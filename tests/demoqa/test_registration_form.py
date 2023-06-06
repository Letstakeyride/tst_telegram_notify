import allure
from selene import have, by

from conftest import RESOURCE_PATH


@allure.title("Successful fill form")
def test_filling_out_the_form(setup_browser):
    browser = setup_browser


    with allure.step("Open registrations form"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Fill form"):
        browser.element('#firstName').type('Mariya')
        browser.element('#lastName').type('Petrova')
        browser.element('#userEmail').type('PevRot@mail.ru')
        browser.element('[for=gender-radio-2]').click()
        browser.element('#userNumber').type(7922691865)
        browser.element('.react-datepicker__input-container').click()
        browser.element('.react-datepicker__month-select ').click()
        browser.element('.react-datepicker__month-select  [value="1"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select  [value="1985"]').click()
        browser.element('.react-datepicker__week [aria-label="Choose Monday, February 4th, 1985"]').click()
        browser.element('#subjectsContainer').click()
        browser.element('#subjectsInput').type('English').press_enter()
        browser.element('[for=hobbies-checkbox-1]').click()
        browser.element('#uploadPicture').set_value(f'{RESOURCE_PATH}/foto.jpg')
        browser.element('#currentAddress').type('Voroshiliva')
        browser.element('#react-select-3-input').type('Haryana').press_enter()
        browser.element('#react-select-4-input').type('Panipat').press_enter()
        browser.element('#submit').click()

    with allure.step("Check form results"):
        browser.all('tbody tr').should(have.exact_texts(
            'Student Name Mariya Petrova', 'Student Email PevRot@mail.ru', 'Gender Female', 'Mobile 7922691865',
            'Date of Birth 04 February,1985', 'Subjects English', 'Hobbies Sports',
            'Picture foto.jpg', 'Address Voroshiliva', 'State and City Haryana Panipat'))