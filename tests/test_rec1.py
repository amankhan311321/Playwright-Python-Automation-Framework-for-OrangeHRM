import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.locator("body").click()
    page.goto("https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fq%3Dbwow%2Bunisex%2Bsalon%26oq%3Dbwow%2Bunisex%2Bsalon%26gs_lcrp%3DEgZjaHJvbWUyBggAEEUYOdIBCDk1OThqMGoyqAIAsAIB%26sourceid%3Dchrome%26ie%3DUTF-8%26sei%3DeZwBao3gBJj-p84Pva7zsAI&q=EgRzYiM8GPm4htAGIjCVzbusb8TxprKAARomw-4C1DcpHVmzokQYjMgg5_hw52Y3jzA4yi9ChBhxVDrL6-EyAVJaAUM")
    page.locator("iframe[name=\"a-e251rmp8r8wq\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.locator("[id=\"7\"]").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.locator("[id=\"8\"]").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.locator("[id=\"0\"]").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.locator("[id=\"8\"]").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.locator("[id=\"7\"]").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.get_by_role("button", name="Verify").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.locator("[id=\"4\"]").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.locator("[id=\"5\"]").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.locator("[id=\"9\"]").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.locator("[id=\"13\"]").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.get_by_role("button", name="Next").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.locator("[id=\"10\"]").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.get_by_role("button", name="Verify").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.locator("[id=\"4\"]").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.locator("[id=\"2\"]").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.locator("[id=\"8\"]").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.locator("[id=\"8\"]").click()
    page.locator("iframe[name=\"c-e251rmp8r8wq\"]").content_frame.get_by_role("button", name="Verify").click()
    page.goto("https://www.google.com/search?q=bwow+unisex+salon&oq=bwow+unisex+salon&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDk1OThqMGoyqAIAsAIB&sourceid=chrome&ie=UTF-8&sei=sJwBavuTG4CSseMPg9P5gAI")
