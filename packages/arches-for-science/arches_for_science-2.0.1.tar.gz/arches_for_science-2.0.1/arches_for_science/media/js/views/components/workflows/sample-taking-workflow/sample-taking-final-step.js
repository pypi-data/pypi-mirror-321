define([
    'geojson-extent',
    'knockout',
    'leaflet',
    'uuid',
    'arches',
    'views/components/workflows/summary-step',
    'templates/views/components/iiif-popup.htm',
    'templates/views/components/workflows/sample-taking-workflow/sample-taking-final-step.htm'
], function(geojsonExtent, ko, L, uuid, arches, SummaryStep, iiifPopup, sampleTakingFinalStepTemplate) {

    function viewModel(params) {
        var self = this;

        this.map = ko.observable();
        this.maps = ko.observableArray();

        this.selectedAnnotationTileId = ko.observable();

        params.form.resourceId(params.samplingActivityResourceId);

        SummaryStep.apply(this, [params]);

        this.findStatementType= function(statements, type){
            var foundStatement = statements.find(function(statement) {
                return statement.type.indexOf(type) > -1;
            });
            return foundStatement ? foundStatement.statement : "None";
        };

        this.tableConfig = {
            "info": false,
            "paging": false,
            "scrollCollapse": true,
            "searching": false,
            "ordering": false,
            "type": "html",
            "columns": [
                null,
                null,
                null,
            ]
        };

        this.prepareAnnotation = function(featureCollection) {
            var canvas = featureCollection.features[0].properties.canvas;

            var afterRender = function(map) {
                L.tileLayer.iiif(canvas + '/info.json').addTo(map);
                var extent = geojsonExtent(featureCollection);
                map.addLayer(L.geoJson(featureCollection, {
                    pointToLayer: function(feature, latlng) {
                        return L.circleMarker(latlng, feature.properties);
                    },
                    style: function(feature) {
                        return feature.properties;
                    },
                    onEachFeature: function(feature, layer) {
                        const classificationConcepts = Object.freeze({
                            // Concept IDs, not values
                            "a2588fa8-5ae6-4770-a473-dec0c05fb175": 'Analysis Area',
                            "2703e524-b5ea-4548-bea7-7ce354e4e05a": 'Sample Area',
                            "9db724b9-b3c7-4761-9a50-673d64a15bd8": 'Sample',
                        });
                        if (!feature.properties.active){
                            var popup = L.popup({
                                closeButton: false,
                                maxWidth: 250
                            })
                                .setContent(iiifPopup)
                                .on('add', function() {
                                    // hope that translator has not adjusted the location of the bracket.
                                    const titleArray = feature.properties.locationName.split('[');
                                    const title = titleArray[0].trim();
                                    const type = classificationConcepts[feature.properties.classificationConceptId];
                                    const parent = feature.properties.parentPhysicalThingName;
                                    const description = (
                                        arches.translations.existingAnnotation
                                        .replace('{title}', title)
                                        .replace('{type}', type)
                                        .replace('{parent}', parent)
                                    );
                                    var popupData = {
                                        closePopup: function() {
                                            popup.remove();
                                        },
                                        name: feature.properties.locationName,
                                        description: description,
                                        // TODO(i18n) slug or name?
                                        graphName: 'Physical Thing',
                                        resourceinstanceid: feature.properties.sampleAreaResourceId,
                                        reportURL: arches.urls.resource_report
                                    };
                                    var popupElement = popup.getElement()
                                        .querySelector('.mapboxgl-popup-content');
                                    ko.applyBindingsToDescendants(popupData, popupElement);
                                });
                            layer.bindPopup(popup);
                        }
                        layer.on('click', function() {
                            if (feature.properties && feature.properties.tileId && feature.properties.active){
                                self.highlightAnnotation(feature.properties.tileId);
                            }
                        });
                    }
                }));
                L.control.fullscreen().addTo(map);
                setTimeout(function() {
                    map.fitBounds([
                        [extent[1]-1, extent[0]-1],
                        [extent[3]+1, extent[2]+1]
                    ]);
                }, 250);
                self.maps.push(map);
            };

            return {
                center: [0, 0],
                crs: L.CRS.Simple,
                zoom: 0,
                afterRender: afterRender
            };
        };

        this.highlightAnnotation = function(tileId){
            if (tileId !== self.selectedAnnotationTileId()){
                self.selectedAnnotationTileId(tileId);
            } else {
                self.selectedAnnotationTileId(null);
            }
            if (self.maps()) {
                self.maps().forEach(function(map){
                    map.eachLayer(function(layer){
                        if (layer.eachLayer) {
                            layer.eachLayer(function(feature){
                                const defaultColor = feature.feature.properties.color;
                                if (self.selectedAnnotationTileId() === feature.feature.properties.tileId) {
                                    feature.setStyle({color: '#BCFE2B', fillColor: '#BCFE2B'});
                                } else {
                                    feature.setStyle({color: defaultColor, fillColor: defaultColor});
                                }
                            });
                        }
                    });
                });
            }
        };

        // get resourceData of the sampling activity
        this.resourceData.subscribe(function(val){ // 1st request
            this.displayName = val.displayname;
            this.reportVals = {
                projectName: {'name': arches.translations.project, 'value': this.getResourceValue(val.resource, ['part of','@display_value'])},
                sampledObjectName: {'name': arches.translations.sampledObject, 'value': this.getResourceValue(val.resource['Sampling Unit'][0], ['Sampling Area','Overall Object Sampled','@display_value'])},
                samplers: {'name': arches.translations.samplers, 'value': this.getResourceValue(val.resource, ['carried out by','@display_value'])},
                samplingDate: {'name': arches.translations.samplingDate, 'value': this.getResourceValue(val.resource, ['TimeSpan','TimeSpan_begin of the begin','@display_value'])},
                samplingActivityName: {'name':  arches.translations.samplingName, 'value': this.getResourceValue(val.resource['Name'][0], ['Name_content','@display_value'])},
            };

            var statements = val.resource['Statement'].map(function(val){
                return {
                    statement:  self.getResourceValue(val, ['Statement_content','@display_value']),
                    type: self.getResourceValue(val, ['Statement_type','@display_value'])
                };
            });
            var samplingTechnique = self.findStatementType(statements, "description,brief text");
            var samplingMotivation = self.findStatementType(statements, "sampling motivation");
            this.reportVals.technique = {'name': arches.translations.samplingTechnique, 'value': samplingTechnique};
            this.reportVals.motivation = {'name': arches.translations.samplingMotivation, 'value': samplingMotivation};
            let sampleAnnotationCollection = {};
            let partsAnnotationCollection = {};

            // get the annotation of the samples and prepare the annotation "sampleAnnotationCollection"
            const sampleUnits = self.getResourceValue(val.resource, ["Sampling Unit"]);
            sampleUnits.forEach(function(unit){
                if (unit['Sample Created']['@display_value']) {
                    var locationName = self.getResourceValue(unit, ['Sample Created','@display_value']);
                    var sampleResourceId = self.getResourceValue(unit, ['Sample Created','resourceId']);
                    var sampleAreaResourceId = self.getResourceValue(unit, ['Sampling Area','resourceId']);
                    var locationAnnotationString = self.getResourceValue(unit, ['Sampling Area','Sampling Area Identification','Sampling Area Visualization','@display_value']);
                    var tileId = self.getResourceValue(unit, ['Sampling Area','Sampling Area Identification','Sampling Area Visualization','@tile_id']);
                    if (locationAnnotationString) {
                        const locationAnnotation = JSON.parse(locationAnnotationString.replaceAll("'",'"'));
                        const canvas = locationAnnotation.features[0].properties.canvas;
                        locationAnnotation.features.forEach(function(feature){
                            feature.properties.active = true;
                            feature.properties.tileId = tileId;
                        });
                        if (canvas in sampleAnnotationCollection) {
                            sampleAnnotationCollection[canvas].push({
                                tileId: tileId,
                                locationName: locationName,
                                sampleResourceId: sampleResourceId,
                                sampleAreaResourceId: sampleAreaResourceId,
                                locationAnnotation: locationAnnotation,
                            });
                        } else {
                            sampleAnnotationCollection[canvas] = [{
                                tileId: tileId,
                                locationName: locationName,
                                sampleResourceId: sampleResourceId,
                                sampleAreaResourceId: sampleAreaResourceId,
                                locationAnnotation: locationAnnotation,
                            }];
                        }
                    }
                }
            });

            // get the parent physical thing's all the parts and prepare the annotation "partsAnnotationCollection"
            const parentPhyiscalThingResourceId = self.getResourceValue(val.resource["Sampling Unit"][0], ['Sampling Area','Overall Object Sampled','resourceId']);
            const parentPhyiscalThing = ko.observable();
            self.getResourceData(parentPhyiscalThingResourceId, parentPhyiscalThing);
            parentPhyiscalThing.subscribe(async function(val) { // 2nd request
                const parts = self.getResourceValue(val.resource, ['Part Identifier Assignment']);
                for (const part of parts) {
                    const locationName = self.getResourceValue(part,['Part Identifier Assignment_Physical Part of Object','@display_value']);
                    const tileId = self.getResourceValue(part,['@tile_id']);
                    const partResourceId = self.getResourceValue(part,['Part Identifier Assignment_Physical Part of Object','resourceId']);
                    const partsAnnotationString = self.getResourceValue(part,['Part Identifier Assignment_Polygon Identifier','@display_value']);
                    if (partsAnnotationString) {
                        const locationAnnotation = JSON.parse(partsAnnotationString.replaceAll("'",'"'));
                        const canvas = locationAnnotation.features[0].properties.canvas;
                        // TODO: fetch in parallel
                        await fetch(self.urls.api_resources(partResourceId) + '?format=json&compact=false&v=beta')
                        .then(response => response.json())
                        .then(data => {
                            locationAnnotation.features.forEach(function(feature) {
                                feature.properties.active = false;
                                feature.properties.tileId = tileId;
                                feature.properties.locationName = locationName;
                                // misnomer, could be analysis area
                                feature.properties.sampleAreaResourceId = partResourceId;
                                feature.properties.classificationConceptId = data.resource.type.concept_details[0].concept_id;
                                feature.properties.parentPhysicalThingName = parentPhyiscalThing().resource._label?.['@display_value'] ?? '';
                            });
                            if (canvas in partsAnnotationCollection) {
                                partsAnnotationCollection[canvas].push({
                                    locationAnnotation: locationAnnotation,
                                    sampleAreaResourceId: partResourceId,
                                });
                            } else {
                                partsAnnotationCollection[canvas] = [{
                                    locationAnnotation: locationAnnotation,
                                    sampleAreaResourceId: partResourceId,
                                }];
                            }
                        });
                    }
                }

                // add the annotation of parts to the final object
                self.annotationStatus = ko.observable();
                //self.sampleAnnotations = ko.observableArray();
                self.sampleAnnotations = [];
                const numberOfCanvases = Object.keys(sampleAnnotationCollection).length;
                let canvasCounter = 0;
                for (const canvas in sampleAnnotationCollection) {
                    let samplingLocations = ko.observableArray();
                    let annotationCombined;
                    const sampleArearResourceIds = sampleAnnotationCollection[canvas].map(sample => sample.sampleAreaResourceId);
                    partsAnnotationCollection[canvas].forEach(function(part){
                        if (!sampleArearResourceIds.includes(part.sampleAreaResourceId)){
                            if (annotationCombined) {
                                annotationCombined.features = annotationCombined.features.concat(part.locationAnnotation.features);
                            } else {
                                annotationCombined = part.locationAnnotation;
                            }
                            part.locationAnnotation.features.forEach(feature => {
                                feature.properties.color = '#999999';
                                feature.properties.fillColor = '#999999';
                            });
                        }
                    });
    
                    // get the sample information from sample resource instance (physical thing) and add to the final object
                    let annotationCounter = 0;
                    sampleAnnotationCollection[canvas].forEach(function(annotation){
                        var sampleResourceId = annotation.sampleResourceId;
    
                        if (annotationCombined) {
                            annotationCombined.features = annotationCombined.features.concat(annotation.locationAnnotation.features);
                        } else {
                            annotationCombined = annotation.locationAnnotation;
                        }
    
                        self.currentLocation = ko.observable();
                        const numberOfAnnotations = sampleAnnotationCollection[canvas].length;

                        self.getResourceData(sampleResourceId, self.currentLocation);
                        self.currentLocation.subscribe(function(val){ // 3rd request
                            var samplingLocationName = val.displayname;
                            if (val.resource["Statement"]){
                                var statements = val.resource["Statement"].map(function(statement){
                                    return {
                                        statement: self.getResourceValue(statement, ['Statement_content','@display_value']),                        
                                        type: self.getResourceValue(statement, ['Statement_type','@display_value'])
                                    };
                                });
                                var sampleMotivation = self.findStatementType(statements, "sampling motivation").replace( /(<([^>]+)>)/ig, '');
                                var sampleDescription = self.findStatementType(statements, "sample description").replace( /(<([^>]+)>)/ig, '');
                            }
                            samplingLocations.push(
                                {
                                    tileId: annotation.tileId,
                                    sampleResourceId: annotation.sampleResourceId,
                                    sampleAreaResourceId: annotation.sampleAreaResourceId,
                                    samplingLocationName: samplingLocationName || "None",
                                    sampleDescription: sampleDescription || "None",
                                    sampleMotivation: sampleMotivation || "None",
                                }
                            );
                            annotationCounter += 1;
                            if (annotationCounter === numberOfAnnotations) {
                                self.annotationStatus.valueHasMutated();
                            }
                        });
                    });
                    self.annotationStatus.subscribe(function(){
                        var leafletConfig = self.prepareAnnotation(annotationCombined);
                        self.sampleAnnotations.push({
                            samplingLocations: samplingLocations,
                            leafletConfig: leafletConfig,
                            featureCollection: annotationCombined,
                        });
                        canvasCounter += 1;
                        if (canvasCounter === numberOfCanvases) {self.loading(false);}
                    });
                }    
            });
        }, this);
    }

    ko.components.register('sample-taking-final-step', {
        viewModel: viewModel,
        template: sampleTakingFinalStepTemplate
    });
    return viewModel;
});
