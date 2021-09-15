from django.shortcuts import redirect, render
from django.contrib import messages
from scipy.sparse import data
from home.models import*

from sklearn.linear_model import LinearRegression
import random
import pandas as pd
from datetime import date, datetime


# for all user
def terms_and_condition_page(request):
    return render(request, 'terms_and_condition.html')

def privacy_policy_page(request):
    return render(request, 'privacy.html')

#guest user -------------------------------------------------------------------------

# Create your views here.
# index page
def indexPage(request):
    stock_data = []
    try:
        stock_data = Stock_model.objects.all()[:4]
        # stock_data = Stock_model.objects.get(id = 5)
    except Stock_model.DoesNotExist as e:
        return render(request, 'index.html', {"stock_data":stock_data})

    return render(request, 'index.html', {"stock_data":stock_data})


#for user login page
def loginPage(request):
    if request.method == "POST":
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        if user_email and user_password:
            try:
                user = User_model.objects.get(email=user_email, password=user_password)
                request.session['Email'] = user.email
                request.session['Name'] = user.name
                request.session['User'] = 'user'
                request.session['ID'] = user.id
                messages.warning(request, "success_login")
                return redirect('/user_page')
            except User_model.DoesNotExist as e:
                messages.warning(request, "email_or_pass_wrong")
        else:
            messages.warning(request, 'input_not_valid')
    else:
        messages.warning(request, 'other', extra_tags='tags')
    return render(request, 'login.html')

# for forget password
def forget_password_page(request):
    if request.method == "POST":
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        user_password_confirm = request.POST['user_password_confirm']
        otp = request.POST['otp']
        if user_email and user_password and user_password_confirm and otp:
            if user_password != user_password_confirm:
                messages.warning(request, "pass_dont_match")
            elif otp != '123456':
                messages.warning(request, "otp_missmatch")
            else:
                try:
                    save_user = User_model.objects.get(email=user_email)
                    save_user.password = user_password
                    messages.warning(request, "update_success")
                    save_user.save()
                    return redirect('/login')
                except User_model.DoesNotExist as e:
                    messages.warning(request, "email_wrong")
        else:
            messages.warning(request, 'input_not_valid')
    else:
        messages.warning(request, 'other', extra_tags='tags')
    return render(request, 'forget_pass.html')

# for singup page
def signupPage(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        user_phone = request.POST['user_phone']
        user_dob	= request.POST['user_dob']
        user_profession = request.POST['user_profession']
        user_address = request.POST['user_address']
        if user_name and user_email and user_password and user_phone and user_dob and user_profession and user_address :
            try:
                user = User_model.objects.get(email=user_email)
                messages.warning(request, user.email+" allready exits..! ")
            except User_model.DoesNotExist as e:
                save_user = User_model()
                save_user.name = user_name
                save_user.email = user_email
                save_user.password = user_password
                save_user.phone = user_phone
                save_user.dob = user_dob
                save_user.profession = user_profession
                save_user.address = user_address
                save_user.save()
                messages.success(request, "signup_success")
                return redirect('/login')
        else:
            messages.warning(request, 'input_not_valid')
    else:
        messages.warning(request, 'signup_others')
    return render(request, 'signup.html')


# User page ----------------------------------------------------------------------------------------------------

#for userPage
def userPage(request):
    stock_data = []
    try:
        stock_data = Stock_model.objects.all()[:4]
    except Stock_model.DoesNotExist as e:
        return render(request, 'userhome.html', {"stock_data":stock_data})
    return render(request, 'userhome.html', {"stock_data":stock_data})

#for profilePage
def profilePage(request):
    user_email  = request.session['Email']
    user = User_model.objects.get(email=user_email)
    return render(request, 'profile.html', {'user':user})

#for profilePage
def edituserprofilePage(request):
    user_email  = request.session['Email']
    save_user = User_model.objects.get(email=user_email)

    if request.method == "POST":
        user_name = request.POST['user_name']
        user_phone = request.POST['user_phone']
        user_dob	= request.POST['user_dob']
        user_profession = request.POST['user_profession']
        user_address = request.POST['user_address']

        save_user.name = user_name
        save_user.phone = user_phone
        # save_user.dob = user_dob
        save_user.profession = user_profession
        save_user.address = user_address
        save_user.save()
        messages.success(request, "update_success")

    return render(request, 'edituserprofile.html', {'user':save_user})


#for stockPage
def stockPage(request):
    stock_data = Stock_model.objects.all()
    return render(request, 'stock.html', {'stock_data':stock_data} )

def stockViewPage(request, id):
    stock = Stock_model.objects.get(id = id)
    predict_list = []
    num_of_dates = 7

    # for predict value of it
    l = []
    l.append("Day "+ str(1)+" (today)")
    l.append(stock.last)

    predict = model_prediction(stock)

    predict_list.append(l)
    max = stock.last
    can_bid = False
    # print(predict)
    # random.seed(10)
    # predict aroud num_of_dates includes
    
    for i in range(2, num_of_dates+1):
        l = []
        l.append("Day "+ str(i))
        r = random.uniform(0, 1)
        val = round( (stock.last * r * predict[0] * 1.2), 3)
        if i == 2:
            max = val
        elif(max<val):
            max = val
        # val = (stock.last * r * predict)
        l.append(val)
        predict_list.append(l)
    max_prediction = round(((max - stock.last)/stock.last)*100, 2)

    if max_prediction>0 :
        can_bid = True
    today = date.today().strftime("%B %d, %Y")
    return render(request, 'stock_view.html', {'stock':stock, 'predict_list': predict_list, 'max_prediction': max_prediction, 'can_bid': can_bid, 'today':today})

# for my stock view
def my_stockViewPage(request, id):
    stock = Stock_model.objects.get(id = id)
    predict_list = []
    num_of_dates = 7

    # for predict value of it
    l = []
    l.append("Day "+ str(1)+" (today)")
    l.append(stock.last)

    predict = model_prediction(stock)

    predict_list.append(l)
    max = stock.last
    can_bid = False
    # print(predict)
    # random.seed(10)
    # predict aroud num_of_dates includes
    
    for i in range(2, num_of_dates+1):
        l = []
        l.append("Day "+ str(i))
        r = random.uniform(0, 1)
        val = round( (stock.last * r * predict[0] * 1.2), 3)
        if i == 2:
            max = val
        elif(max<val):
            max = val
        # val = (stock.last * r * predict)
        l.append(val)
        predict_list.append(l)
    max_prediction = round(((max - stock.last)/stock.last)*100, 2)

    if max_prediction>0 :
        can_bid = True
    today = date.today().strftime("%B %d, %Y")
    return render(request, 'my_stocks_view.html', {'stock':stock, 'predict_list': predict_list, 'max_prediction': max_prediction, 'can_bid': can_bid, 'today':today})


#for my stock page
def myStocksPage(request):
    user_id  = request.session['ID']
    all_data = []
    try:
        bid =  Bid_model.objects.all().filter(USERid = user_id)
        for x in bid:
            stock = Stock_model.objects.get(id = x.STOCKid)
            all_data.append(stock)
    except Bid_model.DoesNotExist as e:
        return render(request, 'mystocks.html', {'stock_data':all_data, 'haveData':False} )
    have_data = False
    if all_data:
        have_data = True
    return render(request, 'mystocks.html', {'stock_data':all_data, 'haveData':have_data} )




## for add data to bid value
def bid_to_stock(request, id1, id2):
    try:
        bid = Bid_model.objects.get(USERid=id1, STOCKid=id2)
        # print(id2)
        messages.warning(request, "Stock"+" allready Bid..! ")
        return redirect('/stockView/'+str(id2))
    except Bid_model.DoesNotExist as e:
        bid = Bid_model()
        bid.USERid = id1
        bid.STOCKid = id2
        bid.save()
        return redirect('/stock')


## sold item and delete form my list
def sold_stock(request, id1, id2):
    bid = Bid_model.objects.get(USERid=id1, STOCKid=id2 )
    bid.delete()
    # messages.warning(request, "sold_success")
    return redirect("/mystocks")

# for logout
def logout(request):
    try:
        del request.session['Email']
        del request.session['Name']
        del request.session['User']
        del request.session['ID']
    except:
        return render(request, 'user.html')
    return redirect("/")


# Admin ...................................................................................................
#for adminPage
def admin_indexPage(request):
    # try:
    #     del request.session['Email']
    #     del request.session['Name']
    #     del request.session['User']
    #     del request.session['ID']
    # except:
    #     return render(request, 'admin_index.html')
    return render(request, 'admin_index.html')


#for admin login
def adminloginPage(request):
    if request.method == "POST":
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        if user_email and user_password:
            try:
                user = Admin_model.objects.get(email=user_email, password=user_password)
                request.session['Email'] = user.email
                request.session['Name'] = user.name
                request.session['Admin'] = 'Admin'
                messages.warning(request, "success_login")
                return redirect('/adminhome')
            except Admin_model.DoesNotExist as e:
                messages.warning(request, "email_or_pass_wrong")
        else:
            messages.warning(request, 'input_not_valid')
    else:
        messages.warning(request, 'other', extra_tags='tags')
    return render(request, 'adminlogin.html')

#for admin homepage
def adminhomePage(request):
    user_data = User_model.objects.all()
    return render(request, 'adminhome.html', {'user_data':user_data})

#for admin all user
def adminAllUserPage(request):
    user_data = User_model.objects.all()
    have_data = False
    for x in user_data:
        have_data = True
        break
    return render(request, 'admin_all_user.html', {'user_data':user_data, 'have_data':have_data})

def adminprofilePage(request):
    user_email  = request.session['Email']
    user = Admin_model.objects.get(email=user_email)
    return render(request, 'adminprofile.html', {'user':user})


# for logout
def adminlogoutPage(request):
    try:
        del request.session['Email']
        del request.session['Name']
        del request.session['Admin']
    except:
        return render(request, 'user.html')
    return redirect("/")

#for view profile
def adminViewUserPage(request, id):
    user = User_model.objects.get(id = id)
    return render(request, 'view_user.html', {'user':user})

# for edit profile
def adminEditUserPage(request, id):
    save_user = User_model.objects.get(id = id)
    if request.method == "POST":
        user_name = request.POST['user_name']
        user_phone = request.POST['user_phone']
        user_dob	= request.POST['user_dob']
        user_profession = request.POST['user_profession']
        user_address = request.POST['user_address']

        save_user.name = user_name
        save_user.phone = user_phone
        # save_user.dob = user_dob
        save_user.profession = user_profession
        save_user.address = user_address
        save_user.save()
        messages.success(request, "update_success")
    return render(request, 'admin_user_profile_edit.html', {'user':save_user})


# for admin show stock data
def admin_stockPage(request):
    stock_data = Stock_model.objects.all()
    return render(request, 'admin_stock.html', {'stock_data':stock_data} )


# for adding a stock
def admin_add_stockPage(request):
    if request.method == "POST":

        today = datetime.now()
        day = today.strftime("%Y-%m-%d")
        time = today.strftime('%H:%M:%S')

        stock = Stock_model()
        name = request.POST['name']
        last = request.POST['last']
        high = request.POST['high']
        low = request.POST['low']
        change_price = request.POST['change_price']
        changePercent = request.POST['changePercent']
        vol = request.POST['vol']
        details = request.POST['details']

        stock.name = name 
        stock.last = last
        stock.high = high 
        stock.low = low 
        stock.change_price =  change_price 
        stock.changePercent = changePercent 
        stock.vol =  vol 
        stock.change_time = time
        stock.change_date = day
        stock.details = details 

        # print(details)

        stock.save()
        messages.success(request, "add_stock_success")
    return render(request, 'admin_add_stock.html')

def admin_view_user_stock_page(request, id):
    user_id  = id
    all_data = []
    user = User_model.objects.get(id = user_id)
    user_name = user.name
    try:
        bid =  Bid_model.objects.all().filter(USERid = user_id)
        for x in bid:
            stock = Stock_model.objects.get(id = x.STOCKid)
            all_data.append(stock)
    except Bid_model.DoesNotExist as e:
        return render(request, 'admin_view_user_stock.html', {'stock_data':all_data, 'haveData':False, 'user_name':user_name} )
    have_data = False
    if all_data:
        have_data = True
    return render(request, 'admin_view_user_stock.html', {'stock_data':all_data, 'haveData':have_data, 'user_name':user_name} )



# for delete user
def adminDeleteStockPage(request, id):
    stock = Stock_model.objects.get(id = id)
    stock.delete()
    return redirect("/admin_stock")


def adminUpdateStockPage(request, id):
    stock = Stock_model.objects.get(id = id)
    if request.method == "POST":
        name = request.POST['name']
        last = request.POST['last']
        high = request.POST['high']
        low = request.POST['low']
        change_price = request.POST['change_price']
        changePercent = request.POST['changePercent']
        vol = request.POST['vol']
        details = request.POST['details']

        stock.name = name 
        stock.last = last
        stock.high = high 
        stock.low = low 
        stock.change_price =  change_price 
        stock.changePercent = changePercent 
        stock.vol =  vol 
        stock.details = details 

        # print(details)

        stock.save()
        messages.success(request, "update_success")
    return render(request, 'admin_stock_update.html', {'stock':stock} )

# for delete user
def adminDeleteUserPage(request, id):
    user = User_model.objects.get(id = id)
    user.delete()
    return redirect("/adminhome")


# for single stock data
def adminstockViewPage(request, id):
    stock = Stock_model.objects.get(id = id)
    predict_list = []
    num_of_dates = 7

    # for predict value of it
    l = []
    l.append("Day "+ str(1)+" (today)")
    l.append(stock.last)

    predict = model_prediction(stock)

    predict_list.append(l)
    max = stock.last
    can_bid = False
    # print(predict)
    # random.seed(10)
    # predict aroud num_of_dates includes
    
    for i in range(2, num_of_dates+1):
        l = []
        l.append("Day "+ str(i))
        r = random.uniform(0, 1)
        val = round( (stock.last * r * predict[0] * 1.2), 3)
        if i == 2:
            max = val
        elif(max<val):
            max = val
        # val = (stock.last * r * predict)
        l.append(val)
        predict_list.append(l)
    max_prediction = round(((max - stock.last)/stock.last)*100, 2)

    if max_prediction>0 :
        can_bid = True
    today = date.today().strftime("%B %d, %Y")
    return render(request, 'admin_stock_view.html', {'stock':stock, 'predict_list': predict_list, 'max_prediction': max_prediction, 'can_bid': can_bid, 'today':today})


# -------------------------------------------------------------------------------------------------------------------------------------------
# this one use for model precdicton....
def model_prediction(stock):
    import numpy as np
    input_path = 'home\model_feed.csv'
    df = pd.read_csv(input_path)
    df = df.replace('-', 0)
    df = df = df.replace(',','', regex=True)

    lr = LinearRegression() # make linerar regression model

    X_train = df[['change_price', 'changePercent', 'vol', 'high', 'low']]
    Y_train = df['last']
    # print(Y_train)
    lr.fit(X_train,Y_train)  #fit the model

    X_test = np.array([[stock.change_price, stock.changePercent, stock.vol, stock.high, stock.low]])
    y_predict = abs(lr.predict(X_test)) / 100 #to nomalize the data devide by 100
    
    return y_predict





# --------------------------------------------------------------------------------------------------------------------------------
# only for data input from csv only don't have other use.
import time
def addStockData(request):
    input_path = 'home/data_for_ast.csv'
    # print(input_path)
    # data = [input_path]
    df = pd.read_csv(input_path)
    # data.append(df.head)
    n = len(df)
    data = []
    count = 0

    import datetime
    date_str = '26/08/2021' # The date
    format_str = '%d/%m/%Y' # The format
    datetime_obj = datetime.datetime.strptime(date_str, format_str)

    for i in range(0, n):
        name = df['name'][i]
        last = df['last'][i]
        high = df['high'][i]
        low	= df['low'][i]
        change_price = df['change_price'][i]
        changePercent = df['changePercent'][i]
        vol	= df['vol'][i]
        change_time	= df['change_time'][i]
        change_date = datetime_obj
        details = df['company_details'][i]

        print(change_date)
        stock = Stock_model()
        stock.name = name
        stock.last = last
        stock.high = high	
        stock.low	= low	
        stock.change_price = change_price
        stock.changePercent = changePercent
        stock.vol	= vol.replace(',', '')
        stock.change_time	= change_time
        stock.change_date = change_date
        stock.details = details

        stock.save()
        count += 1
        time.sleep(1)
        print("Add: ", count)
        data.append("Save")
    
    return render(request, 'module\stockadd.html', {'data':data})




# def table_show(request):
#     return render(request, 'test_table.html')