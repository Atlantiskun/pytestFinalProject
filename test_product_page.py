import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo', [pytest.param(f"promo=offer{i}", marks=pytest.mark.xfail) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_added_to_cart()