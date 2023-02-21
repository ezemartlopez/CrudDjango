def calculate_users_page(total_users,users_by_page,number_page):
    list_a = [users_by_page for x in range(1,int(total_users/users_by_page)+1)]

    if((total_users % users_by_page) != 0):
        list_a.append(total_users % users_by_page)
    
    if(number_page == 1):
        return list_a[0]
    
    return sum(list_a[0:number_page])
