from warehouse_manager.models.database.customer import Customer
from warehouse_manager.models.database.warehouse import Warehouse
from warehouse_manager.services.google_maps import get_location_distance


class TestGoogleMapsService:
    def setup_method(self) -> None:
        self.warehouse = Warehouse(name="Warehouse test 1", latitude=-27.700660693470407, longitude=-48.50131010311051)
        self.customer = Customer(name="Destination 1", latitude=-27.69953233146274, longitude=-48.51088762083777)

    def test_distance_between_warehouse_and_customer(self) -> None:
        result_distance = get_location_distance(self.warehouse, self.customer)

        assert result_distance["distance"] == "2.0 km"
        assert result_distance["duration"] == "5 mins"
