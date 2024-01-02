from features.get_element import get_element as ge
#  this file contains all payment gateways and i can call it from setup form

class payment_gateways:
        
    def bank_transfer(drivers,data):
        trasaction_id = data["tr_id"]
        bank_name = data['bankname']
        holdername = data['holdername']
        note = data['note']
        plan_locator = data['plan_locator']
        bank_locator = data["bank_locator"]
        bank_identified = data["bank_identified"]
        tr_id_add =ge.findelement(drivers,bank_identified[0],bank_locator[0],"send_keys",trasaction_id)
        bank_name_add =ge.findelement(drivers,bank_identified[1],bank_locator[1],"send_keys",bank_name)
        account_name_add =ge.findelement(drivers,bank_identified[2],bank_locator[2],"send_keys",holdername)
        note_add =ge.findelement(drivers,bank_identified[3],bank_locator[3],"send_keys",note)
        return 1
        
        
        
        
    def paypal():
        pass
        # currently not adding any code because i have no https website
    
    def select_plan():
        pass
    
    def select_payment():
        pass