from django.shortcuts import render, redirect

# Create your views here.

Database=[]

def show(request):
    return render(request, 'home.html', {'users':Database})


def post(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname') 
        midname=request.POST.get('midname')   
        lastname=request.POST.get('lastname')
        gender=request.POST.get('gender')
        age=request.POST.get('age') 
        email=request.POST.get('email')   
        phonenumber=request.POST.get('phonenumber')
        education=request.POST.get('education') 
        New_Entry={'id':len(Database)+1, 'firstname':firstname, 'midname':midname, 'lastname':lastname, 'gender':gender,
        'age':age,'email':email, 'phonenumber':phonenumber, 'education':education}
        Database.append(New_Entry)
        return redirect('showinfo')   
    return render(request, 'create.html', {'users':Database})

def put(request, user_id):
    global Database
    if request.method=='POST':
        for user in Database:
            if user['id']==user_id:
                user['firstname']=request.POST.get('firstname') 
                user['midname']=request.POST.get('midname')   
                user['lastname']=request.POST.get('lastname')
                user['gender']=request.POST.get('gender')
                user['age']=request.POST.get('age') 
                user['email']=request.POST.get('email')   
                user['phonenumber']=request.POST.get('phonenumber')
                user['education']=request.POST.get('education') 
        return redirect('showinfo')
    return render(request, 'create.html', {'users':Database})

def drop(request, user_id):
    global Database
    new_data=[]
    if request.method=='POST':
        for user in Database:
            if user['id'] != user_id:
                new_data+=[user]
        Database=new_data
    return redirect('showinfo')
