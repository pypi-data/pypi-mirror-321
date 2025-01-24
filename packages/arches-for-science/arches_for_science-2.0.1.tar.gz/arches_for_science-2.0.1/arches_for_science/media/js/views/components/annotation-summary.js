define([
    'knockout', 
    'geojson-extent',
    'leaflet',
    'arches',
    'templates/views/components/annotation-summary.htm',
    'viewmodels/widget',
    'views/components/iiif-viewer',
    'bindings/leaflet',
    'bindings/datatable',
], function(ko, geojsonExtent, L, arches, annotationSummaryTemplate) {
    return ko.components.register('views/components/annotation-summary', {
        viewModel: function(params) {
            var self = this;

            this.map = ko.observable();
            this.selectedAnnotationTileId = ko.observable();
            this.annotationTableConfig = {
                "info": false,
                "paging": false,
                "scrollCollapse": true,
                "searching": false,
                "ordering": false,
                "columns": [
                    null,
                    null,
                ]
            };
            const popupHtml = `
            <div class="mapboxgl-popup-content">
                <button class="mapboxgl-popup-close-button" type="button" aria-label="${arches.translations.closePopup}" data-bind="click: closePopup">×</button>
                <div class="hover-feature-title-bar">
                    <div class="hover-feature-title">
                        <span class="" data-bind="text: name"></span>
                    </div>
                </div>
                <div class="hover-feature-body">
                    <div class="hover-feature" data-bind="html: description"></div>
                    <div class="hover-feature-metadata">
                        ${arches.translations.resourceModel}:
                        <span data-bind="text: graphName"></span>
                    </div>
                    <div class="hover-feature-metadata">
                        ID:
                        <span data-bind="text: resourceinstanceid"></span>
                    </div>
                </div>
                <div class="hover-feature-footer">
                    <a data-bind="click: function () {
                        window.open(reportURL + resourceinstanceid);
                    }" href="javascript:void(0)">
                        <i class="ion-document-text" aria-hidden="true"></i>
                        ${arches.translations.report}
                    </a>
                </div>
            </div>`;

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
                            if (feature.properties.active === false){
                                var popup = L.popup({
                                    closeButton: false,
                                    maxWidth: 250
                                })
                                    .setContent(popupHtml)
                                    .on('add', function() {
                                        // hope that translator has not adjusted the location of the bracket.
                                        const titleArray = feature.properties.name.split('[');
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
                                            name: feature.properties.name,
                                            description: description,
                                            // TODO(i18n) graph or slug?
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
                                if (feature.properties && feature.properties.tileId && feature.properties.active !== false){
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
                    self.map(map);
                };

                return {
                    center: [0, 0],
                    crs: L.CRS.Simple,
                    zoom: 0,
                    afterRender: afterRender
                };
            };

            this.leafletConfig = this.prepareAnnotation(params.annotation.featureCollection);

            this.highlightAnnotation = function(tileId){
                if (tileId !== self.selectedAnnotationTileId()){
                    self.selectedAnnotationTileId(tileId);
                } else {
                    self.selectedAnnotationTileId(null);
                }
                if (self.map()) {
                    self.map().eachLayer(function(layer){
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
                } 
            };
        },
        template: annotationSummaryTemplate
    });
});
