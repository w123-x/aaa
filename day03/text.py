#   def convert_selector_to_locator(self,selector):
        # '''
        # 'id account' -> By.ID,'account'
        # '''
string='id account'
string=string[3:]
# string=string.__add__('By.ID')
print(string)