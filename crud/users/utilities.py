def calculate_users_page(total_users,users_by_page,number_page):
    """Esta funcion calcula el numero de usuarios que se visualizan por cada pagina de la paginacion. Recibe como parametros:
        1) total_users: el numero de usuarios totales
        2) user_by_page: numero de usuarios que se visualizan por pagina'
        3) number_page: el numero de pagina actual que se esta viendo
    """
    #obtengo cantidad de paginas (num entero)
    divisiones_enteras = int(total_users/users_by_page)
    #creo un array de largo igual ala division entera obtenida donde cada elemento es la cantidad de usuarios por pagina
    list_a = [users_by_page for x in range(1,divisiones_enteras+1)]

    #Si la division no es exacta agrego el resto de usuarios faltantes ala lista
    if((total_users % users_by_page) != 0):
        list_a.append(total_users % users_by_page)
    #si me pide la primera pagina le devuelvo el primer elemento de la lista 
    if(number_page == 1):
        return list_a[0]
    
    #si no entra al if me pide una pagina mayor a 1, y devuelvo la suma del array hasta convenientemente el numero de pagina
    return sum(list_a[0:number_page])
