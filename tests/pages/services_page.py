# pages/services_page.py
from playwright.sync_api import Page, Locator, expect
from .base_page import BasePage


class ServicesPage(BasePage):
    """Encapsulates all interactions and assertions on the /services page."""

    PATH = "/services"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.heading: Locator = page.get_by_role("heading", name="Our Services")
        # Service cards are expected to carry a common class or landmark;
        # falling back to a CSS selector scoped to an article or section role.
        self.service_cards: Locator = page.locator(".service-card")

    def navigate(self) -> None:  # type: ignore[override]
        super().navigate(self.PATH)

    def expect_heading_visible(self) -> None:
        expect(self.heading).to_be_visible()

    def expect_exactly_three_service_cards(self) -> None:
        """Assert that exactly 3 service cards are rendered."""
        expect(self.service_cards).to_have_count(3)

    def expect_each_card_displays_price(self) -> None:
        """Assert that every service card contains a visible price element."""
        for i in range(self.service_cards.count()):
            expect(self.service_cards.nth(i).get_by_test_id("price")).to_be_visible()

    def expect_each_card_has_book_now_link_to_contact(self) -> None:
        """Assert that every service card has a 'Book Now' link pointing to /contact."""
        import re
        for i in range(self.service_cards.count()):
            book_now = self.service_cards.nth(i).get_by_role("link", name="Book Now")
            expect(book_now).to_be_visible()
            expect(book_now).to_have_attribute("href", re.compile(r"/contact"))
