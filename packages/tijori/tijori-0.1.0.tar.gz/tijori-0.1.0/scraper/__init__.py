import os
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Tuple, Dict

# get the environment variables id from the .env file 
id = os.getenv("id")
password = os.getenv("password")

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")

class SeliniumPath:
    url_signin = "https://www.tijorifinance.com/account/signin/"
    signin_button = '//*[@id="account"]/section/div[1]/div/div/div/form/button'
    detailed_forensic_xp = '//*[@id="forensics"]/div/div[2]/div/div[2]/button'
    
    # get_tijori_data
    consolidated_balance_sheet_xp = '//*[@id="balance_sheet"]/section/div[1]/div[2]/ul[1]/li[1]/button'
    consolidated_cash_flow_xp = '//*[@id="cash_flow"]/section/div[1]/div[2]/ul/li[1]/button'
    consolidated_pl_xp = '//*[@id="profit_and_loss"]/section/div[1]/div[2]/ul[1]/li[1]/button'
    consolidated_ratios_xp = '//*[@id="ratios"]/section/div[1]/div[2]/ul/li[1]/button'
    consolidated_quarterly_results_xp = '//*[@id="quarterly_results"]/section/div[1]/div[2]/ul/li[1]/button'
    
    balance_sheet_table = 'balance_sheet_table'
    cash_flow_table = 'cash_flow_table'
    pl_table = 'profit_and_loss_table'
    quarterly_results_table = 'quarterly_results_table'

    ratios_table_wrapper = 'ratios_table_wrapper'
    balance_sheet_table_wrapper = 'balance_sheet_table_wrapper'
    cash_flow_table_wrapper = 'cash_flow_table_wrapper'
    pl_table_wrapper = 'profit_and_loss_table_wrapper'
    quarterly_results_table_wrapper = 'quarterly_results_table_wrapper'
    
    # get_news_updates
    all_updates_xp = '/html/body/div[3]/div[1]/div[7]/div[2]/ul/li[2]/a'
    button_1 = '//*[@id="company_timeline"]/div[2]/button' 
    button_2 = '//*[@id="company_timeline_sidepanel"]/div/div[2]/div[1]/div/button'
    updates_xp = '//*[@id="company_timeline"]/div[2]/button'
    timeline_close_xp = '//*[@id="company_timeline_sidepanel"]/div/div[1]/button'

    read_more_xp = '//*[@id="overview_page_wrapper"]/div[1]/div[1]/div[1]/div[1]/span'
    text_xp = '//*[@id="overview_page_wrapper"]/div[1]/div[1]/div[1]/div[2]'


class SeleniumScraper:
    def __init__(self,id,password):
        self.id = id
        self.password = password
        
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--remote-debugging-port=9222")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(SeliniumPath.url_signin)
    
    def close(self):
        self.driver.quit()
    
    def login(self):
        self.driver.get(SeliniumPath.url_signin)
        time.sleep(1)
        
        self.driver.find_element(By.ID, "email").send_keys(id)
        time.sleep(1)
        try:
            self.driver.find_element(By.ID, "pwd-field").send_keys(password)
            self.driver.find_element(By.XPATH,SeliniumPath.signin_button).click()
            return True
        except:
            try:
                time.sleep(2)
                self.driver.find_element(By.ID, "pwd-field").send_keys(password)
                self.driver.find_element(By.XPATH,SeliniumPath.signin_button).click()
                return True
            except:
                print('Try Manual')
                return False
    
    def company_url_recify(self,company_url:str) -> Tuple[str,str]:
        if company_url[-1] != '/':
            company_url = company_url + '/'
        company = company_url.split('company/')[-1].replace('/','')
        return company_url,company
    
    def get_class_data(self,cname:str,block_cname:str)->List:
        e = self.driver.find_element(By.CLASS_NAME,cname).get_attribute('innerHTML')
        soup = BeautifulSoup(e, 'html.parser')
        blocks = soup.find_all('div', class_=block_cname)
        return blocks
    
    def wait_for_click(self,xpath:str):
        try:
            if len(self.driver.find_elements(By.XPATH,xpath)) < 1:
                print('Wait 3 seconds for consolidated click')
                time.sleep(3)
            else:
                self.driver.find_element(By.XPATH,xpath).click()
        except:
            pass
        try:
            self.driver.find_element(By.XPATH, xpath).click()
        except:
            print('Sleep 3 seconds for detailed click')
            time.sleep(3)
            try:
                self.driver.find_element(By.XPATH, xpath).click()
            except:
                print('Try again : detailed click')
    
    def get_df_table_from_html_parent(self,parent_element:WebElement)-> pd.DataFrame:
        soup = BeautifulSoup(parent_element.get_attribute('innerHTML'), 'html.parser')
        # Extract headers
        headers = []
        for th in soup.select('thead th'):
            header_text = th.get_text(strip=True)
            headers.append(header_text)
        # Extract rows
        rows = []
        for tr in soup.select('tbody tr'):
            row = []
            for td in tr.find_all('td'):
                cell_text = td.get_text(strip=True)
                row.append(cell_text)
            rows.append(row)
        return pd.DataFrame(rows, columns=headers)
    
    def get_df_table(self,table_element:str)-> pd.DataFrame:
        bs = self.driver.find_element(By.ID, table_element).get_attribute('innerHTML')
        df = pd.read_html(bs)[0]
        if 'Unnamed: 1' in df.columns:
            df = df.drop(columns=['Unnamed: 1'])
        df.columns = [i.replace("'",' ') for i in df.columns]
        return df
    
    def navigate_page(self,company_url:str,page:str):
        company_url,_ = self.company_url_recify(company_url)
        if page == 'forensics':
            url = f'{company_url}#forensics'
        if page == 'balance_sheet':
            url = f'{company_url}financials/#balance_sheet'
        if page == 'profit_loss':
            url = f'{company_url}financials/#profit_loss'
        if page == 'cash_flow':
            url = f'{company_url}financials/#cash_flow'
        if page == 'ratios':
            url = f'{company_url}financials/#ratios'
        if page == 'quarterly_results':
            url = f'{company_url}financials/#quarterly_results'
            
        self.driver.get(url)
        time.sleep(3)

    def forensic_details(self) -> Dict:
        #self.navigate_forensic(company_url,page='forensics')
        detailed_forensic_xp = SeliniumPath.detailed_forensic_xp
        if len(self.driver.find_elements(By.XPATH, detailed_forensic_xp)) <1:
            print('sleep 3 seconds')
            time.sleep(3)
        self.wait_for_click(detailed_forensic_xp)
        blocks_forensic_summary =  self.get_class_data('forensic_list','forensic_list__item')
        forensic_details = {}
        for block in blocks_forensic_summary:
            heading = block.find_all('h4')[0].text.replace('\n','')
            fd_sub = {}
            for j in block.find_all('li'):
                sub_heading = j.find('h6').text.replace('\n','')
                data_sub_heading = j.find('p').text.replace('\n','')
                fd_sub[sub_heading] = data_sub_heading
            forensic_details[heading] = fd_sub
            
        return forensic_details

    def ratios_details(self) -> Dict:
        try:
            ratio_blocks = self.get_class_data('quicklook_box_wrapper','quicklook_box')
            ratios_returns = {}
            for r_block in ratio_blocks:
                heading = r_block.find('div', class_='quicklook_box_title').text
                a = r_block.find('div', class_='quicklook_box_content').find_all('div',class_="quicklook_col col_1")
                a = [i.text for i in a]
                b = r_block.find('div', class_='quicklook_box_content').find_all('div',class_="quicklook_col col_2")
                b = [str(i.text).replace('\n','') for i in b]
                ratios_returns[heading] = dict(zip(a,b))
        except:
            ratios_returns = {'NO DATA FOUND'}
        return ratios_returns
    
    def revenue_mix(self) -> Dict:
        rmix_blocks = self.get_class_data('rmix_graph_wrapper','rmix_graph_block')
        rmix = {}
        for block in rmix_blocks:
            heading = block.find_all('h4')[0].text
            div_data = json.loads(block.find_all('div', class_='rmix_pie_chart')[0].get('chart-data'))
            rmix[heading] = div_data
        return rmix
    
    def get_sheet(self,sheet_xp:str,table_xp:str) -> pd.DataFrame:
        #self.navigate_page(company_url,page='balance_sheet')
        element_plus = self.driver.find_element(By.XPATH,sheet_xp)
        if element_plus.get_attribute('class') != 'active':
            time.sleep(3)
            self.wait_for_click(sheet_xp)
        parent_element = self.driver.find_element(By.ID, table_xp) 
        return self.get_df_table_from_html_parent(parent_element)
    
    def get_market_data(self)-> Dict:
        try:
            try:
                self.driver.find_element(By.XPATH,'//*[@id="ms_show_more"]').click()
            except:
                pass
            
            ms_e = self.driver.find_elements(By.CLASS_NAME,'market_share_card')
            ms = {}
            for mse in ms_e:
                soup = BeautifulSoup(mse.get_attribute('innerHTML'),'html.parser')
                val = soup.find_all('div','values_source')[0].text.replace('\n','')
                title = soup.find_all('div','name')[0].text.replace('\n','')
                ms[title] = val
        except:
            print('no market share data')
            ms = {}
        
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, SeliniumPath.timeline_close_xp).click()
        except:
            pass
        return ms
    
    def get_concall_summary(self)-> Dict:
        try:
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            table_kb = soup.find('table', id='companyFilings')
            elements = table_kb.find_all(lambda tag: tag.has_attr('data-target') and tag['data-target'] == '#concall_summary')
            
            concall_summary = {}
            for element in elements:
                summary = json.loads(element.get_attribute_list('data-content')[0])
                year = element.get_attribute_list('data-year')[0]
                month = element.get_attribute_list('data-month')[0]
                concall_summary[year+'-'+month] = summary
        except:
            time.sleep(5)
            try:
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                table_kb = soup.find('table', id='companyFilings')
                elements = table_kb.find_all(lambda tag: tag.has_attr('data-target') and tag['data-target'] == '#concall_summary')
                
                concall_summary = {}
                for element in elements:
                    summary = json.loads(element.get_attribute_list('data-content')[0])
                    year = element.get_attribute_list('data-year')[0]
                    month = element.get_attribute_list('data-month')[0]
                    concall_summary[year+'-'+month] = summary
            except:
                concall_summary = {}    
        return concall_summary
    
    def about_company(self)-> str:
        try:
            self.driver.find_element(By.XPATH,SeliniumPath.read_more_xp).click()
            about_company_str = self.driver.find_element(By.XPATH,SeliniumPath.text_xp).text
        except:
            about_company_str = 'No Data Found'
        return about_company_str
    
    def all_finincials_details(self,company_url:str):
        #Forensic Details
        self.navigate_page(company_url,page='forensics')
        forensic_details = self.forensic_details()
        ratios_returns = self.ratios_details()
        revenue_mix = self.revenue_mix()
        
        time.sleep(1)
        
        # Balance Sheet
        self.navigate_page(company_url,page='balance_sheet')
        bs = self.get_sheet(sheet_xp=SeliniumPath.consolidated_balance_sheet_xp,table_xp=SeliniumPath.balance_sheet_table)
        
        time.sleep(1)
        
        # Profit and Loss
        self.navigate_page(company_url,page='profit_loss')
        pl = self.get_sheet(sheet_xp=SeliniumPath.consolidated_pl_xp,table_xp=SeliniumPath.pl_table)

        time.sleep(1)
        
        # Cash Flow
        self.navigate_page(company_url,page='cash_flow')
        cf = self.get_sheet(sheet_xp=SeliniumPath.consolidated_cash_flow_xp,table_xp=SeliniumPath.cash_flow_table)
        
        time.sleep(1)
        
        # Ratios
        self.navigate_page(company_url,page='ratios')
        dr = self.get_df_table(SeliniumPath.ratios_table_wrapper)
        if 'Unnamed: 0' in dr.columns:
            dr.rename(columns={'Unnamed: 0':'Ratio'},inplace=True)
        time.sleep(1)
        
        # Quarterly Results
        self.navigate_page(company_url,page='quarterly_results')
        qr = self.get_sheet(sheet_xp=SeliniumPath.consolidated_quarterly_results_xp,table_xp=SeliniumPath.quarterly_results_table)

        self.driver.get(company_url)
        time.sleep(2)
        
        market_share = self.get_market_data()
        concall_summary = self.get_concall_summary()
        about = self.about_company()
        
        return {'forensic_details':forensic_details,'ratios_returns':ratios_returns,'revenue_mix':revenue_mix,'balance_sheet':bs,'profit_loss':pl,'cash_flow':cf,'ratios':dr,'quarterly_results':qr,'market_share':market_share,'concall_summary':concall_summary,'about':about}
        