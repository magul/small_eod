from test_plus.test import TestCase

from ...generic.tests.test_views import GenericViewSetMixin, OrderingViewSetMixin
from ...search.tests.mixins import SearchQueryMixin
from ..factories import ChannelFactory
from ..serializers import ChannelSerializer


class ChannelViewSetTestCase(
    GenericViewSetMixin, OrderingViewSetMixin, SearchQueryMixin, TestCase
):
    basename = "channel"
    serializer_class = ChannelSerializer
    factory_class = ChannelFactory
    ordering_fields = [
        "name",
        "postal_code",
    ]

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)
