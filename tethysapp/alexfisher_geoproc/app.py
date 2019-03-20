from tethys_sdk.base import TethysAppBase, url_map_maker


class AlexfisherGeoproc(TethysAppBase):
    """
    Tethys app class for ArcMap and Geoprocessing App.
    """

    name = 'Tethys Geoprocessing App'
    index = 'alexfisher_geoproc:home'
    icon = 'alexfisher_geoproc/images/medal.png'
    package = 'alexfisher_geoproc'
    root_url = 'alexfisher-geoproc'
    color = '#000000'
    description = 'App to demonstrate linking an arcmap and geoprocessing service to a tethys app.'
    tags = '&quot;ArcMap&quot; &quot;Geoprocessing&quot; '
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='alexfisher-geoproc',
                controller='alexfisher_geoproc.controllers.home'
            ),
            UrlMap(
                name='team',
                url='team',
                controller='alexfisher_geoproc.controllers.team'
            ),
            UrlMap(
                name='individual',
                url='individual',
                controller='alexfisher_geoproc.controllers.individual'
            ),
        )

        return url_maps
