import os
import time

from selenium.webdriver import Keys

from generator.generator import *
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators


class FormPage(BasePage):

    def fill_fields_and_submit(self):
        person = generated_person()
        path = generated_file()
        self.remove_footer()
        self.element_is_visible(FormPageLocators.LAST_NAME).send_keys(person.first_name)
        self.element_is_visible(FormPageLocators.FIRS_NAME).send_keys(person.last_name)
        self.element_is_visible(FormPageLocators.EMAIL).send_keys(person.email)
        self.element_is_visible(FormPageLocators.GENDER).click()
        self.element_is_visible(FormPageLocators.MOBILE).send_keys(person.mobile)
        subject = self.element_is_visible(FormPageLocators.SUBJECT)
        subject.send_keys(person.subject)
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(FormPageLocators.HOBBIES).click()
        self.element_is_visible(FormPageLocators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(FormPageLocators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(FormPageLocators.SUBMIT).click()
        return person

    def form_page_result(self):
        result_list = self.elements_are_visible(FormPageLocators.RESULT_TABLE)
        result_text = [i.text for i in result_list]
        # for i in result_list:
        #     result_text.append(i.text)
        return result_text
