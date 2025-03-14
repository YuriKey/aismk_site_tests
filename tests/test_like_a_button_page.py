from pages.like_a_button import LikeAButton


def test_button_exist(browser):
    like_a_button_page = LikeAButton(browser)
    like_a_button_page.open()
    assert like_a_button_page.button_is_displayed, 'Button not found'


def test_button_clicked(browser):
    like_a_button_page = LikeAButton(browser)
    like_a_button_page.open()
    like_a_button_page.button_click()
    assert 'Submitted' == like_a_button_page.result_text
