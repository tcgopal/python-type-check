from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, constr, validator, root_validator
from pydantic.types import conint


class Inovice(BaseModel):
    # id: int
    # name = 'John Doe'
    # signup_ts: Optional[datetime] = None
    # friends: List[int] = []

    COMPANY_CODE: constr(max_length=15)  
    SOURCE_ERP: constr(max_length=20)  
    SUPPLIER_COUNTRY_CODE_ENGLISH: constr(min_length=2, max_length=2)
    COMPANY_ROLE: constr(max_length=1) = "S"  
    INVOICE_TYPE: constr(min_length=11, max_length=50) = "Tax Invoice"
    INVOICE_SUBTYPE: constr(min_length=7, max_length=50)
    TEMPLATE_CODE: constr(max_length=100) = "TAX IN"  
    TRAN_BRANCH: constr(max_length=50) = "" 
    TRAN_SERVICE_BRANCH: constr(max_length=50)  
    ERP_TRANSACTION_REF: constr(max_length=100)  
    TRAN_DOC_TYPE: constr(min_length=2, max_length=2)
    TRAN_DOC_NO: constr(max_length=100)       
    TRAN_DOC_DATE: constr(regex=r'^\d{8}$')
    TRAN_LINE_NO: int
    DATE_OF_SUPPLY: constr(regex=r'^\d{8}$')  
    SUPPLY_FROM_DATE: constr(regex=r'^\d{8}$')  
    SUPPLY_END_DATE: constr(regex=r'^\d{8}$')  
    POSTING_DATE: Optional[constr(regex=r'^\d{8}$')]  
    TAX_CODE: Optional[constr(max_length=100)]  
    PRODUCT_CODE: constr(max_length=50)  
    ITEM_BUYER_IDENTIFICATION: Optional[constr(max_length=127)]  
    ITEM_SELLER_IDENTIFICATION: Optional[constr(max_length=127)]  
    ITEM_STANDARD_IDENTIFY_TYPE: Optional[constr(max_length=127)]  
    ITEM_STANDARD_IDENTIFIER_NO: Optional[constr(max_length=127)]  
    PRODUCT_DESCRIPTION_1_ENGLISH: Optional[constr(max_length=250)]  
    PRODUCT_DESCRIPTION_1_LANG02: Optional[constr(max_length=500)]  
    INV_CURRENCY_CODE: constr(max_length=3) = "SAR"
    VAT_CURRENCY_CODE: constr(max_length=3) = "SAR"
    BANK_AC_HOLDER_NAME: Optional[constr(max_length=100)]  
    BANK_AC_HOLDER_NAME_LANG02: Optional[constr(max_length=250)]  
    COMPANY_BANK_NAME: Optional[constr(max_length=100)]  
    COMPANY_BANK_NAME_LANG02: Optional[constr(max_length=100)]  
    COMPANY_BANK_ADDRESS: Optional[constr(max_length=1000)]  
    COMPANY_BANK_ADDRESS_LANG02: Optional[constr(max_length=1000)]  
    COMPANY_BANK_IBAN: Optional[constr(max_length=50)]  
    COMPANY_SWIFT_CODE: Optional[constr(max_length=50)]  
    COMPANY_BANK_ACCOUNT_NO: Optional[constr(max_length=100)]  
    TRAN_CUST_CODE: constr(max_length=200)  
    CUST_NAME_WALKIN: constr(max_length=1000)  
    CUST_NAME_WALKIN_LANG02: constr(max_length=1000)  
    CUST_VAT_TIN_WALKIN: constr(max_length=25)  
    CUST_VAT_REG_TYP_WALKIN: constr(max_length=10)  
    CUST_VAT_REG_TYP_WALKIN_LANG02: constr(max_length=250)  
    CUST_ADDITIONAL_ID_NO_WALKIN: constr(max_length=100)  
    CUST_ADDL_ID_TYP_WALKIN: constr(max_length=100)  
    CUST_ADDL_ID_TYP_WALKIN_LANG02: constr(max_length=100)  
    CUST_BUILDING_NUMBER_WALKIN: int[conint(max_digits=4)]  
    CUST_ADD_ADDRESS_NO_WALKIN: Optional[int[conint(max_digits=4)]]  
    CUST_ADD1_WALKIN: constr(max_length=500)  
    CUST_ADD1_WALKIN_LANG02: constr(max_length=1000)  
    CUST_ADD2_WALKIN: Optional[constr(max_length=500)]  
    CUST_ADD2_WALKIN_LANG02: Optional[constr(max_length=1000)]  
    CUST_DISTRICT_ENG_WALKIN: Optional[constr(max_length=127)]  
    CUST_DISTRICT_LANG02_WALKIN: Optional[constr(max_length=250)]  
    CUST_CITY_WALKIN: constr(max_length=100)  
    CUST_CITY_WALKIN_LANG02: constr(max_length=250)  
    CUST_PROVINCE_WALKIN: Optional[constr(max_length=100)]  
    CUST_PROVINCE_WALKIN_LANG02: Optional[constr(max_length=250)]  
    CUST_PINCODE_WALKIN: constr(max_length=50)  
    CUST_COUNTRY_WALKIN: constr(min_length=2, max_length=2) 
    CUST_COUNTRY_WALKIN_LANG02: constr(max_length=100)  
    CUST_PRIMARY_EMAIL_ID_WALKIN: constr(max_length=100)  
    TRAN_CUST_ACCNO: Optional[constr(max_length=100)]  
    TRAN_VEN_CODE: Optional[constr(max_length=100)]  
    TRAN_REMARKS: Optional[constr(max_length=2000)]  
    TRAN_REMARKS_LANG02: Optional[constr(max_length=3000)]  
    REASON_NOTES: constr(max_length=1000)  
    TRAN_ORG_DOC_NO: constr(max_length=5000)  
    TRAN_ORG_DOC_DATE: constr(max_length=5000)  
    TRAN_ORG_PRODUCT_CODE: Optional[constr(max_length=50)]  
    TRAN_ORG_TAXABLE_AFT_DISC: Optional[int]  
    TRAN_ORG_TAX_AMOUNT: Optional[int]  
    TRAN_ORG_DOC_VAL: Optional[int]  
    TRAN_UQC: Optional[constr(max_length=127)]  
    TRAN_QUANTITY: int 
    TRAN_UNIT_PRICE: int
    TRAN_TAX_CODE_CATEGORY: constr(max_length=50)  
    TRAN_GROSS_AMOUNT: int 
    TRAN_DISC1_REASON_CODE: constr(max_length=100)  
    TRAN_DISC1_REASON_TEXT: constr(max_length=1000)  
    TRAN_DISC1_PERCENT: int
    TRAN_DISC1_AMOUNT: Optional[int]  
    TRAN_DISC2_REASON_CODE: constr(max_length=100)  
    TRAN_DISC2_REASON_TEXT: constr(max_length=1000)  
    TRAN_DISC2_PERCENT: int  
    TRAN_DISC2_AMOUNT: Optional[int]  
    TRAN_CHGS_REASON_CODE: constr(max_length=100)  
    TRAN_CHGS_REASON_TEXT: constr(max_length=1000)  
    TRAN_CHGS_PERCENT: int  
    TRAN_CHGS_AMOUNT: Optional[int]  
    TRAN_NET_AMOUNT: int
    TRAN_TAX_RATE: int 
    TRAN_TAX_AMOUNT: int 
    TRAN_NET_PLUS_TAX: int
    TRAN_VAT_EXEMPT_REASON_CODE: constr(max_length=100)  
    TRAN_VAT_EXEMPT_REASON_TEXT: constr(max_length=1000)  
    INV_DISC1_TAX_CATEGORY: constr(max_length=1)  
    INV_DISC1_PERCENT: int 
    INV_DISC1_AMOUNT: Optional[int]  
    INV_DISC1_VAT_RATE: int 
    INV_DISC1_VAT_AMOUNT: int
    INV_DISC1_REASON_CODE: constr(max_length=100)  
    INV_DISC1_REASON_TEXT: constr(max_length=1000)  
    INV_DISC2_TAX_CATEGORY: constr(max_length=1)  
    INV_DISC2_PERCENT: int
    INV_DISC2_AMOUNT: Optional[int]  
    INV_DISC2_VAT_RATE: int 
    INV_DISC2_VAT_AMOUNT: int
    INV_DISC2_REASON_CODE: constr(max_length=100)  
    INV_DISC2_REASON_TEXT: constr(max_length=1000)  
    INV_CHGS_TAX_CATEGORY: constr(max_length=1)  
    INV_CHGS_PERCENT: int  
    INV_CHGS_AMOUNT: Optional[int]  
    INV_CHGS_VAT_RATE: int
    INV_CHGS_VAT_AMOUNT: int
    INV_CHGS_REASON_CODE: constr(max_length=100)  
    INV_CHGS_REASON_TEXT: constr(max_length=1000)  
    INV_NET_AMOUNT: int  
    INV_TOTAL_TAX_AMOUNT: int 
    ROUNDING_AMOUNT: Optional[int]  
    INV_TOTAL_AMOUNT: int 
    PREPAID_INV_NO: constr(max_length=100)  
    ORG_PREPAID_ERP_REF_NO: constr(max_length=100)  
    PREPAID_TAXABLE_AMOUNT: int  
    PREPAID_TAX_AMOUNT: int
    PREPAID_VAT_RATE: int  
    PREPAID_VAT_CATEGORY: constr(max_length=1)  
    INV_CUSTOMER_PAID_AMOUNT: int 
    INV_CUSTOMER_AMOUNT_DUE: int
    PAY_METHOD: Optional[constr(max_length=5)]  
    PAY_METHOD_LANG02: Optional[constr(max_length=250)]  
    PAY_TERMS: constr(max_length=250)  
    PAY_TERMS_LANG02: Optional[constr(max_length=250)]  
    PURCHASE_ORDER_ID: Optional[constr(max_length=127)]  
    PO_DATE: Optional[constr(max_length=100)]  
    CONTRACT_ID: Optional[constr(max_length=127)]  
    ADDITIONAL_NOTES: Optional[constr(max_length=1000)]  
    CURRENCY_EXCHNG_RATE: Optional[int]  
    TRAN_ORG_TAXABLE_AFT_DISC_FCY: int
    TRAN_ORG_TAX_AMOUNT_FCY: int  
    TRAN_ORG_DOC_VAL_FCY: int 
    TRAN_UNIT_PRICE_FCY: int
    TRAN_GROSS_AMOUNT_FCY: int
    TRAN_DISC1_AMOUNT_FCY: int
    TRAN_DISC2_AMOUNT_FCY: int
    TRAN_CHGS_AMOUNT_FCY: int
    TRAN_NET_AMOUNT_FCY: int
    TRAN_TAX_AMOUNT_FCY: int 
    TRAN_NET_PLUS_TAX_FCY: int
    INV_DISC1_AMOUNT_FCY: int 
    INV_DISC1_VAT_AMOUNT_FCY: int 
    INV_DISC2_AMOUNT_FCY: int
    INV_DISC2_VAT_AMOUNT_FCY: int
    INV_CHGS_AMOUNT_FCY: int
    INV_CHGS_VAT_AMOUNT_FCY: int
    INV_NET_AMOUNT_FCY: int 
    INV_TOTAL_TAX_AMOUNT_FCY: int
    INV_TOTAL_AMOUNT_FCY: int 
    PREPAID_TAXABLE_AMOUNT_FCY: int
    PREPAID_TAX_AMOUNT_FCY: int 
    ROUNDING_AMOUNT_FCY: Optional[int]  
    INV_CUSTOMER_PAID_AMOUNT_FCY: int 
    INV_CUSTOMER_AMOUNT_DUE_FCY: int  
    Invoice_Counter: Optional[int]  
    UUID: Optional[constr(max_length=250)]  
    QR_CODE: Optional[constr(max_length=700)] 

    @validator(TRAN_DOC_DATE, DATE_OF_SUPPLY, SUPPLY_FROM_DATE, SUPPLY_END_DATE, POSTING_DATE)
    def parse_date(cls, value):
        try:
            # return datetime.strptime(value, '%Y%m%d').date()
            return value
        except ValueError:
            raise ValueError("Invalid date format. Expected 'YYYYMMDD'.")
        
    
    # @validator(
    #     POSTING_DATE,
    #     TAX_CODE,
    #     ITEM_BUYER_IDENTIFICATION,
    #     ITEM_SELLER_IDENTIFICATION,
    #     ITEM_STANDARD_IDENTIFY_TYPE,
    #     ITEM_STANDARD_IDENTIFIER_NO,
    #     PRODUCT_DESCRIPTION_1_ENGLISH,
    #     PRODUCT_DESCRIPTION_1_LANG02,
    #     BANK_AC_HOLDER_NAME,
    #     BANK_AC_HOLDER_NAME_LANG02,
    #     COMPANY_BANK_NAME,
    #     COMPANY_BANK_NAME_LANG02,
    #     COMPANY_BANK_ADDRESS,
    #     COMPANY_BANK_ADDRESS_LANG02,
    #     COMPANY_BANK_IBAN,
    #     COMPANY_SWIFT_CODE,
    #     COMPANY_BANK_ACCOUNT_NO,
    #     CUST_ADD_ADDRESS_NO_WALKIN,
    #     CUST_ADD2_WALKIN,
    #     CUST_ADD2_WALKIN_LANG02,
    #     CUST_DISTRICT_ENG_WALKIN,
    #     CUST_DISTRICT_LANG02_WALKIN,
    #     CUST_PROVINCE_WALKIN,
    #     CUST_PROVINCE_WALKIN_LANG02,
    #     TRAN_CUST_ACCNO,
    #     TRAN_VEN_CODE,
    #     TRAN_REMARKS,
    #     TRAN_REMARKS_LANG02,
    #     TRAN_ORG_PRODUCT_CODE,
    #     TRAN_ORG_TAXABLE_AFT_DISC,
    #     TRAN_ORG_TAX_AMOUNT,
    #     TRAN_ORG_DOC_VAL,
    #     TRAN_UQC,
    #     TRAN_DISC1_AMOUNT,
    #     TRAN_DISC2_AMOUNT,
    #     TRAN_CHGS_AMOUNT,
    #     INV_DISC1_AMOUNT,
    #     INV_DISC2_AMOUNT,
    #     INV_CHGS_AMOUNT,
    #     ROUNDING_AMOUNT,
    #     PAY_METHOD,
    #     PAY_METHOD_LANG02,
    #     PAY_TERMS_LANG02,
    #     PURCHASE_ORDER_ID,
    #     PO_DATE,
    #     CONTRACT_ID,
    #     ADDITIONAL_NOTES,
    #     CURRENCY_EXCHNG_RATE,
    #     ROUNDING_AMOUNT_FCY,
    #     Invoice_Counter,
    #     UUID,
    #     QR_CODE
    # )
    # def parse_date(cls, value):
    #     try:
    #         return value
    #     except ValueError:
    #         raise ValueError("Invalid date format. Expected 'YYYYMMDD'.")

    @root_validator
    def validate_instances(cls, values):
        

        return values

    # def pre(self, **values):

    #     return values

    

external_data = {'id': '123', 'signup_ts': '2017-06-01 12:22', 'friends': [1, '2', b'3']}
user = Inovice(**external_data)
print(user)
#> User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)