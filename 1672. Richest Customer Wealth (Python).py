class Solution(object):
    def maximumWealth(self, accounts):
        wealth = sum(accounts[0]) # Initializing wealth with 1st customer's wealth

        # looping over every customer's wealth and comparing it.
        for i in accounts:
            if sum(i) > wealth:
                wealth = sum(i)
              
        return wealth
