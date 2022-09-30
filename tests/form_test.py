from pages.form_page import FormPage


class TestFormPage:

    def test_form(self, browser):
        form_page = FormPage(browser, f"{browser.base_url}/automation-practice-form")
        form_page.open()
        person = form_page.fill_fields_and_submit()
        result = form_page.form_page_result()
        assert f'{person.first_name} {person.last_name}' == result[0], 'The form has not been field'
        assert person.email == result[1], 'The form has not been field'
