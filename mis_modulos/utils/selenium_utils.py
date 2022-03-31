# import module
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.chrome.service import Service
from tkinter import Tk


def translate_java_to_python(text_list, name):
    """
    This function takes a list of strings and a name as input.
    It then converts the list of strings to a string and then uses the string to create a python file with the name given.
    The python file is then saved in the output folder.
    The function returns nothing.

    Parameters:
        text_list (list): A list of strings.
        name (str): The name of the python file to be created.

    Example:
        >>> text_list = ['public class HelloWorld {', 'public static void main(String[] args) {', 'System.out.println("Hello, World");', '}', '}']
        >>> name = 'HelloWorld'
        >>> translate_java_to_python(text_list, name)
    """

    if '__' in name:
        name = name.replace('__', '')

    # Create the webdriver object. Here the
    # chromedriver is present in the driver
    # folder of the root directory.
    s = Service("/home/lorty/chromedriver")
    driver = webdriver.Chrome(service=s)

    # get https://www.geeksforgeeks.org/
    driver.get("https://kalkicode.com/ai/online-java-to-python-converter")

    # Maximize the window and let code stall
    # for 10s to properly maximise the window.
    # driver.maximize_window()
    # time.sleep(10)

    # Obtain the input text
    try:
        input_textarea = driver.find_element(By.ID, 'input')
        input_textarea.clear()

        for line in text_list:
            input_textarea.send_keys(line + '\n')

        name_textarea = driver.find_element(By.ID, 'code_class')
        name_textarea.clear()
        name_textarea.send_keys(name)

        input_button = driver.find_element(By.ID, 'submitCode')
        input_button.click()
    except:
        driver.close()
        translate_java_to_python(text_list, name)

    try:
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'code_output'), 'class'), 'finish')

        output_button = driver.find_element(By.ID, 'copy_output')
        driver.execute_script("arguments[0].scrollIntoView(true);", output_button)
        output_button.click()
        python_parsed = Tk().clipboard_get()
        str('python_parsed:' + python_parsed)

        python_parsed = python_parsed.split('\n')

        with open(str('/home/lorty/Escritorio/etsiinf/Trabajo/easy2read/guideline6Vocab/modules/utils_modules/json/jsonschema2pojo/output/' + name + '.py'), 'w') as f:
            start = 0
            if python_parsed:
                if isinstance(python_parsed, list):
                    for parsed_line in python_parsed:
                        if isinstance(parsed_line, str):
                            if 'sb = java.lang.StringBuilder()' in parsed_line:
                                parsed_line = parsed_line.replace('sb =  java.lang.StringBuilder()', 'sb = []')

                            elif 'sb =  java.lang.StringBuilder()' in parsed_line:
                                parsed_line = parsed_line.replace('sb =  java.lang.StringBuilder()', 'sb = []')

                            elif 'sb  = java.lang.StringBuilder()' in parsed_line:
                                parsed_line = parsed_line.replace('sb  = java.lang.StringBuilder()', 'sb = []')

                            elif 'sb  =  java.lang.StringBuilder()' in parsed_line:
                                parsed_line = parsed_line.replace('sb  =  java.lang.StringBuilder()', 'sb = []')

                            elif '.class.getName()).append(\'@\').append(str(hex(System.identityHashCode(self.this)))).append(\'[\')' in parsed_line:
                                if ' .class.getName()).append(\'@\').append(str(hex(System.identityHashCode(self.this)))).append(\'[\')' in parsed_line:
                                    parsed_line = '# deleted'
                                if '__' in parsed_line:
                                    parsed_line = parsed_line.replace('__', '')
                                parsed_line = '# deleted'
                                
                            elif '.getName()).append(\'@\').append(Integer.toHexString(System.identityHashCode(this))).append(\'[\');' in parsed_line:
                                if ' .getName()).append(\'@\').append(Integer.toHexString(System.identityHashCode(this))).append(\'[\');' in parsed_line:
                                    parsed_line = '# deleted'
                                if '__' in parsed_line:
                                    parsed_line = parsed_line.replace('__', '')
                                parsed_line = parsed_line.replace(
                                    '.getName()).append(\'@\').append(Integer.toHexString(System.identityHashCode(this))).append(\'[\');',
                                    '')
                                
                            elif 'if (sb.charAt((sb.length() - 1)) == \',\') :' in parsed_line:
                                parsed_line = '# deleted'
                                
                            elif 'sb.setCharAt((sb.length() - 1),\']\')' in parsed_line:
                                parsed_line = '# deleted'
                                
                            elif 'else :' in parsed_line:
                                parsed_line = '# deleted'
                                
                            elif 'sb.append(\'[\')' in parsed_line:
                                parsed_line = '# deleted'
                                
                            elif 'sb.append(\']\')' in parsed_line:
                                parsed_line = '# deleted'
                                
                            elif 'return sb.toString()' in parsed_line:
                                parsed_line = '# deleted'

                            elif 'sb.append' in parsed_line:
                                parsed_line = parsed_line + '\n        print(str(sb))'
                                

                            for i in range(0, len(parsed_line)):
                                subparsed_line = parsed_line[i:len(parsed_line)]
                                if re.search('(sb.append\(([A-Z]))\w+.', subparsed_line):
                                    parsed_line = '# deleted'
                                elif re.search('(\.append\(\'[A-Z!"·$%&/()=|@#~½¬{]\'\))', subparsed_line):
                                    parsed_line = '# deleted'
                                elif re.search('(\.append\(\"[A-Z!"·$%&/()=|@#~½¬{]\"\))', subparsed_line):
                                    parsed_line = '# deleted'
                                elif re.search('(getName\(\)\)\.append\(\'.\'\)\.append\([A-Za-z0-9().{}]+\.append\(\'.\'\);)', subparsed_line):
                                    parsed_line = '# deleted'
                                elif re.search('(getName\(\)\)\.append\(\'.\'\)\.append\([A-Za-z0-9().{}]+\.append\(.\);)', subparsed_line):
                                    parsed_line = '# deleted'
                                elif re.search('(getName\(\)\)\.append\(.\)\.append\([A-Za-z0-9().{}]+\.append\(\'.\'\);)', subparsed_line):
                                    parsed_line = '# deleted'
                                elif re.search('(getName\(\)\)\.append\(.\)\.append\([A-Za-z0-9().{}]+\.append\(.\);)', subparsed_line):
                                    parsed_line = '# deleted'
                                elif re.search('(\.class\.getName\(\)\)\.append\(\'.\'\)\.append\([A-Za-z0-9().{}]+\.append\(\'.\'\);)', subparsed_line):
                                    parsed_line = '# deleted'
                                elif re.search('(\.class\.getName\(\)\)\.append\(\'.\'\)\.append\([A-Za-z0-9().{}]+\.append\(.\);)', subparsed_line):
                                    parsed_line = '# deleted'
                                elif re.search('(\.class\.getName\(\)\)\.append\(.\)\.append\([A-Za-z0-9().{}]+\.append\(\'.\'\);)', subparsed_line):
                                    parsed_line = '# deleted'
                                elif re.search('(\.class\.getName\(\)\)\.append\(.\)\.append\([A-Za-z0-9().{}]+\.append\(.\);)', subparsed_line):
                                    parsed_line = '# deleted'

                            if parsed_line != '# deleted':
                                f.write(parsed_line + '\n')
    except:
        translate_java_to_python(text_list, name)

    driver.close()

