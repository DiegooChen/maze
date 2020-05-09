# -*- coding:utf-8 -*-

import glob
import os
import shutil
import time

# 导入Selenium库
from selenium import webdriver

maze_store_path = r'E:\Mazes\SVG'
dld_folder = r'C:\Users\fjort\Downloads\*'


def get_number():
    pass


def download_maze(configuration, original_file, time_stamp, maze_type):
    dld_file = ''
    move_to_file = ''

    print('Latest file name: %s' % original_file)

    file_ext = os.path.splitext(original_file)[1]

    flag_start_dl = False
    flag_comp_dl = False

    while not flag_start_dl:
        new_file = max(glob.iglob(dld_folder), key=os.path.getctime)
        new_ext = os.path.splitext(new_file)[1]

        print('Not started downloaded yet.')
        print('New file: ', new_file)

        if new_file != original_file:
            if new_ext == '.crdownload' or new_ext == '.tmp' or new_ext == '.svg':
                flag_start_dl = True
                print('Start download')

                # 循环直到下载完成
                while not flag_comp_dl:
                    new_file = max(glob.iglob(dld_folder), key=os.path.getctime)
                    new_ext = os.path.splitext(new_file)[1]

                    print('Downloading... Lateste file ext ', new_ext)
                    if new_ext == '.svg':
                        flag_comp_dl = True
                        dld_file = new_file
                        print('Download completed.')
                    time.sleep(0.5)
        time.sleep(0.5)

    if maze_type == 'p':
        move_to_file = maze_store_path + '\\' + configuration + time_stamp + '_P.svg'
        print('Move to File Name: ', move_to_file)

    elif maze_type == 's':
        move_to_file = maze_store_path + '\\' + configuration + time_stamp + '_S.svg'
        print('Move to File Name: ', move_to_file)

    shutil.move(dld_file, move_to_file)


def gen_maze(driver, config):
    # 选择迷宫形状
    driver.find_element_by_xpath('//*[@id="ShapeDropDownList"]').click()
    driver.find_element_by_xpath('//*[@id="ShapeDropDownList"]/option[1]').click()

    driver.find_element_by_xpath('//*[@id="S1WidthTextBox"]').clear()
    driver.find_element_by_xpath('//*[@id="S1WidthTextBox"]').send_keys('40')

    driver.find_element_by_xpath('//*[@id="S1HeightTextBox"]').clear()
    driver.find_element_by_xpath('//*[@id="S1HeightTextBox"]').send_keys('40')

    driver.find_element_by_xpath('//*[@id="AlgorithmParameter1TextBox"]').clear()
    driver.find_element_by_xpath('//*[@id="AlgorithmParameter1TextBox"]').send_keys('50')

    driver.find_element_by_xpath('//*[@id="AlgorithmParameter2TextBox"]').clear()
    driver.find_element_by_xpath('//*[@id="AlgorithmParameter2TextBox"]').send_keys('50')

    driver.find_element_by_xpath('//*[@id="GenerateButton"]').click()

    # time.sleep(2)
    time_stamp = time.strftime('%Y%m%d%H%M%S')

    # Download puzzle
    driver.find_element_by_xpath('//*[@id="FileFormatSelectorList"]').click()
    driver.find_element_by_xpath('//*[@id="FileFormatSelectorList"]/option[7]').click()

    ogn_file = max(glob.iglob(dld_folder), key=os.path.getctime)
    driver.find_element_by_xpath('//*[@id="DownloadFileButton"]').click()

    download_maze(config, ogn_file, time_stamp, 'p')

    # Download solution
    driver.find_element_by_xpath('//*[@id="FileFormatSelectorList"]').click()
    driver.find_element_by_xpath('//*[@id="FileFormatSelectorList"]/option[8]').click()

    ogn_file = max(glob.iglob(dld_folder), key=os.path.getctime)
    driver.find_element_by_xpath('//*[@id="DownloadFileButton"]').click()

    download_maze(config, ogn_file, time_stamp, 's')


def get_mazes(config, quantity):
    dr = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    dr.get('http://www.mazegenerator.net/')

    for index in range(quantity):
        gen_maze(dr, config)

    dr.quit()


if __name__ == '__main__':
    conf = "RS01"
    qty = 5
    get_mazes(conf, qty)
