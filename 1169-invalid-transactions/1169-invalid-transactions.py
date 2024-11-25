class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        names = []
        cities = []
        times = []
        amounts = []
        my_dict = {}
        ans = []
        
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            names.append(name)
            times.append(int(time))
            amounts.append(int(amount))
            cities.append(city)
            
            time = int(time)
            if time not in my_dict:
                my_dict[time]= {name:[city]}
            elif name not in my_dict[time]:
                my_dict[time][name] = [city]
            else:
                my_dict[time][name].append(city)
            
        
        for i in range(len(transactions)):
            if amounts[i] > 1000:
                ans.append(transactions[i])
                continue
                
            for j in range(times[i]-60, times[i]+61):
                if j not in my_dict:
                    continue
                if names[i] not in my_dict[j]:
                    continue
                if len(my_dict[j][names[i]])> 1 or (my_dict[j][names[i]][0] != cities[i]):
                    ans.append(transactions[i])
                    break
                
            
        return ans
        