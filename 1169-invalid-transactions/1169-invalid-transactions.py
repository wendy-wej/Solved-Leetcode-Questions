class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        my_dict = {}
        ans = []
        
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            
            
            time = int(time)
            if time not in my_dict:
                my_dict[time]= {name:[city]}
            elif name not in my_dict[time]:
                my_dict[time][name] = [city]
            else:
                my_dict[time][name].append(city)
            
        
        for i in transactions:
            name, time, amount, city = i.split(',')
            time = int(time)
            amount = int(amount)
            if amount > 1000:
                ans.append(i)
                continue
                
            for j in range(time-60, time+61):
                if j not in my_dict:
                    continue
                if name not in my_dict[j]:
                    continue
                if len(my_dict[j][name])> 1 or (my_dict[j][name][0] != city):
                    ans.append(i)
                    break                            
        return ans

## Alternative solution is to use brute force and mark eact satisfied condition as True in a n array of length transactions. Then returning every transaction that is marked True

        