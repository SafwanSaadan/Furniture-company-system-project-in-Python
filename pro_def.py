from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql



#--------------- إنشاء نافذة البرنامج ------------------------
pro = Tk()
pro.geometry('1370x710+1+1')
pro.title('برنامج إدارة مؤسسة مفروشات')
pro.configure(background="silver")
pro.resizable(False,False)
main_frame = Frame(pro, bg='white')
main_frame.place(x=1,y=1,width=1370,height=700)





#---------------------------------------------------- الموظفين : employees ------------------------------------------
#---------------------------------------------------- الموظفين : employees ------------------------------------------

def employees():
        #--------------- إنشاء نافذة البرنامج ------------------------
        
        title = Label(pro ,
        text='[نظام إدارة الموظفين]',
        bg='#1AAECB',
        font=('monospace',16),
        fg='white')
        title.pack(fill=X)

#-----------------------  varible  --------------------
        emp_id =StringVar()
        emp_name =StringVar()
        emp_job =StringVar()
        emp_phone =StringVar()
        emp_address =StringVar()
        emp_salary =StringVar()
        delete_emp =StringVar()
        emp_search =StringVar()
        search_by =StringVar()
        
#--------------------------- أدوات التحكم بالبرنامج ------------------------------
        manage_frame = Frame(pro, bg='white')
        manage_frame.place(x=1137,y=50,width=210,height=400)
        l_id_emp = Label(manage_frame, text='الرقم التسلسي',bg='white')
        l_id_emp.pack()
        id_emp = Entry(manage_frame,textvariable=emp_id, bd='2', justify='center')
        id_emp.pack()
        l_name_emp = Label(manage_frame, text='إسم الموظف',bg='white')
        l_name_emp.pack()
        name_emp = Entry(manage_frame, textvariable=emp_name, bd='2', justify='center')
        name_emp.pack()
        l_job_emp = Label(manage_frame, text=' العمل',bg='white')
        l_job_emp.pack()
        job_emp = Entry(manage_frame, textvariable=emp_job, bd='2', justify='center')
        job_emp.pack()
        l_phone_emp = Label(manage_frame, text='رقم الهاتف',bg='white')
        l_phone_emp.pack()
        phone_emp = Entry(manage_frame,textvariable=emp_phone, bd='2', justify='center')
        phone_emp.pack()
        l_address_emp = Label(manage_frame, text=' العنوان',bg='white')
        l_address_emp.pack()
        address_emp = Entry(manage_frame, textvariable=emp_address, bd='2', justify='center')
        address_emp.pack()
        l_salary_emp = Label(manage_frame, text='راتب الموظف',bg='white')
        l_salary_emp.pack()
        salary_emp = Entry(manage_frame, textvariable=emp_salary, bd='2', justify='center')
        salary_emp.pack()
        l_del_emp = Label(manage_frame, text=' حذف موظف برقم التسلسلي',bg='white', fg='red')
        l_del_emp.place(x=50,y=300)
        del_emp = Entry(manage_frame, textvariable=delete_emp, bd='2', justify='center')
        del_emp.place(x=44,y=330)

        #----------------------- dietals عرض النتائج والبيانات ---------------------------------------------
        dietals_frame = Frame(pro,bg='#F2F4F4')
        dietals_frame.place(x=1,y=102,width=1138,height=605)
        
        #-------- scrollbar ------------------------
        scroll_x = Scrollbar(dietals_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(dietals_frame, orient=VERTICAL)
        
        #-------- treeveiw -------------------------
        employees_table = ttk.Treeview(dietals_frame,
        columns=('emp_salary','emp_address','emp_phone','emp_job','emp_name','emp_id'),
        xscrollcommand = scroll_x.set,
        yscrollcommand = scroll_y.set)
        employees_table.place(x=18,y=1,width=1130,height=587)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)
         #-------- scrollbar  إحتياط---------------------
        scroll_x.config(command=employees_table.xview)
        scroll_y.config(command=employees_table.yview)
        
        
        def get_cursor(ev):
                cursor_row = employees_table.focus()
                contents = employees_table.item(cursor_row)
                row = contents['values']
                emp_salary.set(row[0])     
                emp_address.set(row[1])     
                emp_phone.set(row[2])     
                emp_job.set(row[3])    
                emp_name.set(row[4])     
                emp_id.set(row[5]) 
                
        
        employees_table['show']='headings'
        employees_table.heading('emp_salary',text='راتب الموظف')
        employees_table.heading('emp_address',text=' العنوان')
        employees_table.heading('emp_phone',text='رقم الهاتف')
        employees_table.heading('emp_job',text=' العمل')
        employees_table.heading('emp_name',text='إسم الموظف')
        employees_table.heading('emp_id',text='رقم الموظف')
        
        employees_table.column('emp_address',width=125)
        employees_table.column('emp_salary',width=30)
        employees_table.column('emp_phone',width=65)
        employees_table.column('emp_job',width=65)
        employees_table.column('emp_name',width=150)
        employees_table.column('emp_id',width=20)
        employees_table.bind("<ButtonRelease-1>",get_cursor)

        #------------------- connect database + add --------------------------------------
                    
        def update_employees():
                    conn = pymysql.connect(
                            host = 'localhost',
                            user = 'safwan',
                            password = 'safwan123',
                            database = 'pro_db')
                    cur = conn.cursor()
                    cur.execute("update employees set emp_salary=%s, emp_address=%s , emp_phone=%s, emp_job=%s, emp_name=%s, emp_id=%s",(
                                                                                                                    emp_salary.get(),     
                                                                                                                    emp_address.get(),     
                                                                                                                    emp_phone.get(),     
                                                                                                                    emp_job.get(),     
                                                                                                                    emp_name.get(),     
                                                                                                                    emp_id.get()     
                                                                                                                    ))
                    conn.commit()
                    clear()
                    fetch_all()
                    conn.close()
                    
                    
        def fetch_all():
                    conn = pymysql.connect(
                                    host = 'localhost',
                                    user = 'safwan',
                                    password = 'safwan123',
                                    database = 'pro_db')
                    cur = conn.cursor()
                    cur.execute('select * from employees')
                    rows = cur.fetchall()
                    if len(rows) !=0:
                            employees_table.delete(*employees_table.get_children())
                            for row in rows:
                                    employees_table.insert("",END,value=row)
                    
                            conn.commit()
                    conn.close()
                    
        fetch_all()
        def add_employees():
                    conn = pymysql.connect(
                            host = 'localhost',
                            user = 'safwan',
                            password = 'safwan123',
                            database = 'pro_db')
                    cur = conn.cursor()
                    cur.execute("insert into employees values(%s,%s,%s,%s,%s,%s)",(
                                                                    emp_salary.get(),     
                                                                    emp_address.get(),     
                                                                    emp_phone.get(),     
                                                                    emp_job.get(),     
                                                                    emp_name.get(),     
                                                                    emp_id.get()     
                                                                    ))
                    conn.commit()
                    clear()
                    fetch_all()
                    conn.close()
                    
                    
        def search_employees():
                    conn = pymysql.connect(
                                    host = 'localhost',
                                    user = 'safwan',
                                    password = 'safwan123',
                                    database = 'pro_db')
                    cur = conn.cursor()
                    cur.execute("select * from employees where emp_" +
                    str(search_by.get())+" LIKE '%"+str(emp_search.get())+"%'")
                    rows = cur.fetchall()
                    if len(rows) !=0:
                            employees_table.delete(*employees_table.get_children())
                            for row in rows:
                                    employees_table.insert("",END,value=row)
                    
                            conn.commit()
                    conn.close()
                    
                    
        def delete():
                    conn = pymysql.connect(
                                    host = 'localhost',
                                    user = 'safwan',
                                    password = 'safwan123',
                                    database = 'pro_db')
                    cur = conn.cursor()
                    cur.execute('delete from employees where emp_id=%s',delete_emp.get())
                    conn.commit()
                    fetch_all()
                    conn.close() 
                    
                            
        def clear():
                    emp_salary.set('')     
                    emp_address.set('')     
                    emp_phone.set('')     
                    emp_job.set('')    
                    emp_name.set('')     
                    emp_id.set('')
                    
                    
        def about():
                messagebox.showinfo("devloper Safwan Saadan","welcome to our first project")      
    
#---------------------  buttons  الأزرار -------------------------
        btn_frame = Frame(pro,bg ='white')
        btn_frame.place(x=1137,y=435,width=210,height=353)
        titlel = Label(btn_frame,text='لوحة التحكم', font=('Deco',14),fg='red')
        titlel.pack(fill=X)
        
        add_btn=Button(btn_frame,text='إضافة موظف',bg='green',fg='white', command=add_employees)
        add_btn.place(x=33,y=33,width=150,height=30)
        del_btn=Button(btn_frame,text='حذف موظف',bg='red',fg='white', command=delete)
        del_btn.place(x=33,y=66,width=150,height=30)
        update_btn=Button(btn_frame,text='تعديل بيانات موظف',bg='#3498DB',fg='white', command=update_employees)
        update_btn.place(x=33,y=99,width=150,height=30)
        clear_btn=Button(btn_frame,text='إفراغ الحقول',bg='#85929E',fg='white', command=clear)
        clear_btn.place(x=33,y=132,width=150,height=30)
        about_btn=Button(btn_frame,text='من نحن',bg='#85929E',fg='white', command=about)
        about_btn.place(x=33,y=165,width=150,height=30)
        exit_btn=Button(btn_frame,text='إغلاق البرنامج',bg='red',fg='white', command=pro.quit)
        exit_btn.place(x=33,y=198,width=150,height=30)
        
#---------------------- search manage البحث  -------------------------------------------
        search_frame = Frame(pro,bg='white')
        search_frame.place(x=1,y=50,width=1134,height=50)
        
        l_search = Label(search_frame,text='البحث عن موظف', font=('Deco',14) , fg='red' , bg='white')
        l_search.place(x=1000,y=12)
        
        combo_search = ttk.Combobox(search_frame, textvariable=search_by, justify='right')
        combo_search['value']=('id','name','job','phone','salary')
        combo_search.place(x=900,y=12,width=100,height=25)
        
        search_emp = Entry(search_frame, textvariable=emp_search, justify='right' , bd='2')
        search_emp.place(x=645,y=12,width=250,height=25)
        
        search_btn = Button(search_frame , text='بحث', bg='#3498DB', fg='white', command=search_employees)
        search_btn.place(x=540,y=12,width=100,height=25)
        
        
        
 
 
#---------------------------------------------------- المبيعات : sale --------------------------------------------------
#---------------------------------------------------- المبيعات : sale --------------------------------------------------
       
        
        
def sale():
    #--------------- إنشاء نافذة البرنامج ------------------------
        pro.geometry('1350x690+1+1')
        pro.title('برنامج إدارة الموظفين')
        pro.configure(background="silver")
        pro.resizable(False,False)
        title = Label(pro ,
        text='[نظام إدارة الموظفين]',
        bg='#1AAECB',
        font=('monospace',16),
        fg='white')
        title.pack(fill=X)

#-----------------------  varible  --------------------
        sale_id =StringVar()
        sale_name =StringVar()
        sale_purchase_amount =StringVar()
        sale_date_purchase =StringVar()
        sale_type =StringVar()
        delete_sale =StringVar()
        sale_search =StringVar()
        search_by =StringVar()
        
#--------------------------- أدوات التحكم بالبرنامج ------------------------------
        manage_frame = Frame(pro, bg='white')
        manage_frame.place(x=1137,y=50,width=210,height=400)
        l_id_sale = Label(manage_frame, text='رقم عملية البيع',bg='white')
        l_id_sale.pack()
        id_sale = Entry(manage_frame,textvariable=sale_id, bd='2', justify='center')
        id_sale.pack()
        l_name_sale = Label(manage_frame, text='إسم عملية البيع',bg='white')
        l_name_sale.pack()
        name_sale = Entry(manage_frame, textvariable=sale_name, bd='2', justify='center')
        name_sale.pack()
        l_sale_purchase_amount = Label(manage_frame, text=' مبلغ البيع',bg='white')
        l_sale_purchase_amount.pack()
        sale_purchase_amount = Entry(manage_frame, textvariable=sale_purchase_amount, bd='2', justify='center')
        sale_purchase_amount.pack()
        l_sale_date_purchase = Label(manage_frame, text='تاريخ البيع',bg='white')
        l_sale_date_purchase.pack()
        sale_date_purchase = Entry(manage_frame,textvariable=sale_date_purchase, bd='2', justify='center')
        sale_date_purchase.pack()
        l_sale_type = Label(manage_frame, text=' نوع البيع',bg='white')
        l_sale_type.pack()
        sale_type = ttk.Combobox(manage_frame, textvariable=sale_type, justify='center')
        sale_type['value']=('كاش','أجل')
        sale_type.pack()
        l_del_sale = Label(manage_frame, text=' حذف عملية بيع برقم',bg='white', fg='red')
        l_del_sale.place(x=50,y=300)
        del_sale = Entry(manage_frame, textvariable=delete_sale, bd='2', justify='center')
        del_sale.place(x=44,y=330)
        
        
        #----------------------- dietals عرض النتائج والبيانات ---------------------------------------------
        dietals_frame = Frame(pro,bg='#F2F4F4')
        dietals_frame.place(x=1,y=102,width=1138,height=605)
        
        #-------- scrollbar ------------------------
        scroll_x = Scrollbar(dietals_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(dietals_frame, orient=VERTICAL)
        
        #-------- treeveiw -------------------------
        sale_table = ttk.Treeview(dietals_frame,
        columns=('sale_type','sale_date_purchase','sale_purchase_amount','sale_name','sale_id'),
        xscrollcommand = scroll_x.set,
        yscrollcommand = scroll_y.set)
        sale_table.place(x=18,y=1,width=1130,height=587)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)
         #-------- scrollbar  إحتياط---------------------
        scroll_x.config(command=sale_table.xview)
        scroll_y.config(command=sale_table.yview)
        
        
        def get_cursor(ev):
                cursor_row = sale_table.focus()
                contents = sale_table.item(cursor_row)
                row = contents['values']   
                sale_type.set(row[0])     
                sale_date_purchase.set(row[1])     
                sale_purchase_amount.set(row[2])    
                sale_name.set(row[3])     
                sale_id.set(row[4]) 
        
        sale_table['show']='headings'
        sale_table.heading('sale_type',text=' نوع البيع')
        sale_table.heading('sale_date_purchase',text='تاريخ البيع')
        sale_table.heading('sale_purchase_amount',text=' مبلغ البيع')
        sale_table.heading('sale_name',text='إسم عملية البيع')
        sale_table.heading('sale_id',text='رقم عملية البيع')
        
        sale_table.column('sale_type',width=125)
        sale_table.column('sale_date_purchase',width=65)
        sale_table.column('sale_purchase_amount',width=65)
        sale_table.column('sale_name',width=150)
        sale_table.column('sale_id',width=20)
        sale_table.bind("<ButtonRelease-1>",get_cursor)
        
        
        
        #------------------- connect database + add --------------------------------------
        
        def fetch_all():
                        conn = pymysql.connect(
                                        host = 'localhost',
                                        user = 'safwan',
                                        password = 'safwan123',
                                        database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute('select * from sale')
                        rows = cur.fetchall()
                        if len(rows) !=0:
                                sale_table.delete(*sale_table.get_children())
                                for row in rows:
                                        sale_table.insert("",END,value=row)
                        
                                conn.commit()
                        conn.close()
        
        
        fetch_all()
        def add_sale():
                        conn = pymysql.connect(
                                host = 'localhost',
                                user = 'safwan',
                                password = 'safwan123',
                                database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute("insert into sale values(%s,%s,%s,%s,%s)",(    
                                                                        sale_type.get(),     
                                                                        sale_date_purchase.get(),     
                                                                        sale_purchase_amount.get(),     
                                                                        sale_name.get(),     
                                                                        sale_id.get()     
                                                                        ))
                        conn.commit()
                        clear()
                        fetch_all()
                        conn.close()
                        
                        
        def update_sale():
                        conn = pymysql.connect(
                                host = 'localhost',
                                user = 'safwan',
                                password = 'safwan123',
                                database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute("update sale set sale_type=%s , sale_date_purchase=%s, sale_purchase_amount=%s, sale_name=%s, sale_id=%s",(    
                                                                                                                        sale_type.get(),     
                                                                                                                        sale_date_purchase.get(),     
                                                                                                                        sale_purchase_amount.get(),     
                                                                                                                        sale_name.get(),     
                                                                                                                        sale_id.get()     
                                                                                                                        ))
                        conn.commit()
                        clear()
                        fetch_all()
                        conn.close()
                        
                        
                        
        def search_sale():
                        conn = pymysql.connect(
                                        host = 'localhost',
                                        user = 'safwan',
                                        password = 'safwan123',
                                        database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute("select * from sale where sale_" +
                        str(search_by.get())+" LIKE '%"+str(sale_search.get())+"%'")
                        rows = cur.fetchall()
                        if len(rows) !=0:
                                sale_table.delete(*sale_table.get_children())
                                for row in rows:
                                        sale_table.insert("",END,value=row)
                        
                                conn.commit()
                        conn.close()
                        
                        
        def delete():
                        conn = pymysql.connect(
                                        host = 'localhost',
                                        user = 'safwan',
                                        password = 'safwan123',
                                        database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute('delete from sale where sale_id=%s',delete_sale.get())
                        conn.commit()
                        fetch_all()
                        conn.close() 
                        
                                
        def clear():  
                        sale_type.set('')     
                        sale_date_purchase.set('')     
                        sale_purchase_amount.set('')    
                        sale_name.set('')     
                        sale_id.set('')
                        
                        
                        
        def about():
                messagebox.showinfo("devloper Safwan Saadan","welcome to our first project") 

#---------------------  buttons  الأزرار -------------------------
        btn_frame = Frame(pro,bg ='white')
        btn_frame.place(x=1137,y=435,width=210,height=353)
        titlel = Label(btn_frame,text='لوحة التحكم', font=('Deco',14),fg='red')
        titlel.pack(fill=X)
        
        add_btn=Button(btn_frame,text='إضافة عملية بيع',bg='green',fg='white', command=add_sale)
        add_btn.place(x=33,y=33,width=150,height=30)
        del_btn=Button(btn_frame,text='حذف عملية بيع',bg='red',fg='white', command=delete)
        del_btn.place(x=33,y=66,width=150,height=30)
        update_btn=Button(btn_frame,text='تعديل بيانات البيع',bg='#3498DB',fg='white', command=update_sale)
        update_btn.place(x=33,y=99,width=150,height=30)
        clear_btn=Button(btn_frame,text='إفراغ الحقول',bg='#85929E',fg='white', command=clear)
        clear_btn.place(x=33,y=132,width=150,height=30)
        about_btn=Button(btn_frame,text='من نحن',bg='#85929E',fg='white', command=about)
        about_btn.place(x=33,y=165,width=150,height=30)
        exit_btn=Button(btn_frame,text='إغلاق البرنامج',bg='red',fg='white', command=pro.quit)
        exit_btn.place(x=33,y=198,width=150,height=30)
        
#---------------------- search manage البحث  -------------------------------------------
        search_frame = Frame(pro,bg='white')
        search_frame.place(x=1,y=50,width=1134,height=50)
        
        l_search = Label(search_frame,text='البحث عن عملية بيع', font=('Deco',14) , fg='red' , bg='white')
        l_search.place(x=1000,y=12)
        
        combo_search = ttk.Combobox(search_frame, textvariable=search_by, justify='right')
        combo_search['value']=('id','name','purchase_amount','date_purchase','type')
        combo_search.place(x=900,y=12,width=100,height=25)
        
        search_sale = Entry(search_frame, textvariable=sale_search, justify='right' , bd='2')
        search_sale.place(x=645,y=12,width=250,height=25)
        
        search_btn = Button(search_frame , text='بحث', bg='#3498DB', fg='white', command=search_sale)
        search_btn.place(x=540,y=12,width=100,height=25)
        
        
    
    
    
    
    
#---------------------------------------------------- العملاء : clients ------------------------------------------
#---------------------------------------------------- العملاء : clients ------------------------------------------

def clients():
    #--------------- إنشاء نافذة البرنامج ------------------------

        
        title = Label(pro ,
        text='[ نظام إدارة العملاء ]',
        bg='#1AAECB',
        font=('monospace',16),
        fg='white')
        title.pack(fill=X)

#-----------------------  varible  --------------------
        cli_id =StringVar()
        cli_name =StringVar()
        cli_phone =StringVar()
        cli_address =StringVar()
        delete_cli =StringVar()
        cli_search =StringVar()
        search_by =StringVar()
        
#--------------------------- أدوات التحكم بالبرنامج ------------------------------
        manage_frame = Frame(pro, bg='white')
        manage_frame.place(x=1137,y=50,width=210,height=400)
        l_id_cli = Label(manage_frame, text='الرقم التسلسي',bg='white')
        l_id_cli.pack()
        id_cli = Entry(manage_frame,textvariable=cli_id, bd='2', justify='center')
        id_cli.pack()
        l_name_cli = Label(manage_frame, text='إسم العميل',bg='white')
        l_name_cli.pack()
        name_cli = Entry(manage_frame, textvariable=cli_name, bd='2', justify='center')
        name_cli.pack()
        l_phone_cli = Label(manage_frame, text='رقم الهاتف',bg='white')
        l_phone_cli.pack()
        phone_cli = Entry(manage_frame,textvariable=cli_phone, bd='2', justify='center')
        phone_cli.pack()
        l_address_cli = Label(manage_frame, text=' العنوان',bg='white')
        l_address_cli.pack()
        address_cli = Entry(manage_frame, textvariable=cli_address, bd='2', justify='center')
        address_cli.pack()
        l_del_cli = Label(manage_frame, text=' حذف عميل برقم التسلسلي',bg='white', fg='red')
        l_del_cli.place(x=50,y=300)
        del_cli = Entry(manage_frame, textvariable=delete_cli, bd='2', justify='center')
        del_cli.place(x=44,y=330)
        
        
        #----------------------- dietals عرض النتائج والبيانات ---------------------------------------------
        dietals_frame = Frame(pro,bg='#F2F4F4')
        dietals_frame.place(x=1,y=102,width=1138,height=605)
        
        #-------- scrollbar ------------------------
        scroll_x = Scrollbar(dietals_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(dietals_frame, orient=VERTICAL)
        
        #-------- treeveiw -------------------------
        clients_table = ttk.Treeview(dietals_frame,
        columns=('cli_address','cli_phone','cli_name','cli_id'),
        xscrollcommand = scroll_x.set,
        yscrollcommand = scroll_y.set)
        clients_table.place(x=18,y=1,width=1130,height=587)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)
         #-------- scrollbar  إحتياط---------------------
        scroll_x.config(command=clients_table.xview)
        scroll_y.config(command=clients_table.yview)
        
        
        def get_cursor(ev):
                cursor_row = clients_table.focus()
                contents = clients_table.item(cursor_row)
                row = contents['values']   
                cli_address.set(row[0])     
                cli_phone.set(row[1])        
                cli_name.set(row[2])     
                cli_id.set(row[3])
                
        
        clients_table['show']='headings'
        clients_table.heading('cli_address',text=' العنوان')
        clients_table.heading('cli_phone',text='رقم الهاتف')
        clients_table.heading('cli_name',text='إسم العميل')
        clients_table.heading('cli_id',text='رقم العميل')
        
        clients_table.column('cli_address',width=125)
        clients_table.column('cli_phone',width=65)
        clients_table.column('cli_name',width=150)
        clients_table.column('cli_id',width=20)
        clients_table.bind("<ButtonRelease-1>",get_cursor)
        
        
        #------------------- connect database + add --------------------------------------
        def fetch_all():
                        conn = pymysql.connect(
                                        host = 'localhost',
                                        user = 'safwan',
                                        password = 'safwan123',
                                        database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute('select * from clients')
                        rows = cur.fetchall()
                        if len(rows) !=0:
                                clients_table.delete(*clients_table.get_children())
                                for row in rows:
                                        clients_table.insert("",END,value=row)
                        
                                conn.commit()
                        conn.close()
                        
        
        
        fetch_all()
        def add_clients():
                        conn = pymysql.connect(
                                host = 'localhost',
                                user = 'safwan',
                                password = 'safwan123',
                                database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute("insert into clients values(%s,%s,%s,%s)",(     
                                                                        cli_address.get(),     
                                                                        cli_phone.get(),         
                                                                        cli_name.get(),     
                                                                        cli_id.get()     
                                                                        ))
                        conn.commit()
                        clear()
                        fetch_all()
                        conn.close()
                        
                        
        def update_clients():
                        conn = pymysql.connect(
                                host = 'localhost',
                                user = 'safwan',
                                password = 'safwan123',
                                database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute("update clients set cli_address=%s , cli_phone=%s, cli_name=%s, cli_id=%s",(     
                                                                                                cli_address.get(),     
                                                                                                cli_phone.get(),         
                                                                                                cli_name.get(),     
                                                                                                cli_id.get()     
                                                                                                ))
                        conn.commit()
                        clear()
                        fetch_all()
                        conn.close()
                        
                        
                        
                        
        def search_clients():
                        conn = pymysql.connect(
                                        host = 'localhost',
                                        user = 'safwan',
                                        password = 'safwan123',
                                        database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute("select * from clients where cli_" +
                        str(search_by.get())+" LIKE '%"+str(cli_search.get())+"%'")
                        rows = cur.fetchall()
                        if len(rows) !=0:
                                clients_table.delete(*clients_table.get_children())
                                for row in rows:
                                        clients_table.insert("",END,value=row)
                        
                                conn.commit()
                        conn.close()
                        
                        
        def delete():
                        conn = pymysql.connect(
                                        host = 'localhost',
                                        user = 'safwan',
                                        password = 'safwan123',
                                        database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute('delete from clients where cli_id=%s',delete_cli.get())
                        conn.commit()
                        fetch_all()
                        conn.close() 
                        
                                
        def clear():     
                        cli_address.set('')     
                        cli_phone.set('')       
                        cli_name.set('')     
                        cli_id.set('')
                        
                         
                        
                        
        def about():
                messagebox.showinfo("devloper Safwan Saadan","welcome to our first project")

#---------------------  buttons  الأزرار -------------------------
        btn_frame = Frame(pro,bg ='white')
        btn_frame.place(x=1137,y=435,width=210,height=353)
        titlel = Label(btn_frame,text='لوحة التحكم', font=('Deco',14),fg='red')
        titlel.pack(fill=X)
        
        add_btn=Button(btn_frame,text='إضافة عميل',bg='green',fg='white', command=add_clients)
        add_btn.place(x=33,y=33,width=150,height=30)
        del_btn=Button(btn_frame,text='حذف عميل',bg='red',fg='white', command=delete)
        del_btn.place(x=33,y=66,width=150,height=30)
        update_btn=Button(btn_frame,text='تعديل بيانات عميل',bg='#3498DB',fg='white', command=update_clients)
        update_btn.place(x=33,y=99,width=150,height=30)
        clear_btn=Button(btn_frame,text='إفراغ الحقول',bg='#85929E',fg='white', command=clear)
        clear_btn.place(x=33,y=132,width=150,height=30)
        about_btn=Button(btn_frame,text='من نحن',bg='#85929E',fg='white', command=about)
        about_btn.place(x=33,y=165,width=150,height=30)
        exit_btn=Button(btn_frame,text='إغلاق البرنامج',bg='red',fg='white', command=pro.quit)
        exit_btn.place(x=33,y=198,width=150,height=30)
        
#---------------------- search manage البحث  -------------------------------------------
        search_frame = Frame(pro,bg='white')
        search_frame.place(x=1,y=50,width=1134,height=50)
        
        l_search = Label(search_frame,text='البحث عن عميل', font=('Deco',14) , fg='red' , bg='white')
        l_search.place(x=1000,y=12)
        
        combo_search = ttk.Combobox(search_frame, textvariable=search_by, justify='right')
        combo_search['value']=('id','name','phone','address')
        combo_search.place(x=900,y=12,width=100,height=25)
        
        search_cli = Entry(search_frame, textvariable=cli_search, justify='right' , bd='2')
        search_cli.place(x=645,y=12,width=250,height=25)
        
        search_btn = Button(search_frame , text='بحث', bg='#3498DB', fg='white', command=search_clients)
        search_btn.place(x=540,y=12,width=100,height=25)
        
        
        
        
        

#---------------------------------------------------- المشتتريات : purchase ------------------------------------------
#---------------------------------------------------- المشتتريات : purchase ------------------------------------------

def purchase():
    #--------------- إنشاء نافذة البرنامج ------------------------
        pro.geometry('1350x690+1+1')
        pro.title('برنامج إدارة الموظفين')
        pro.configure(background="silver")
        pro.resizable(False,False)
        title = Label(pro ,
        text='[نظام إدارة الموظفين]',
        bg='#1AAECB',
        font=('monospace',16),
        fg='white')
        title.pack(fill=X)

#-----------------------  varible  --------------------
        pur_id =StringVar()
        pur_name =StringVar()
        pur_purchase_amount =StringVar()
        pur_date_purchase =StringVar()
        pur_type =StringVar()
        delete_pur =StringVar()
        pur_search =StringVar()
        search_by =StringVar()
        
#--------------------------- أدوات التحكم بالبرنامج ------------------------------
        manage_frame = Frame(pro, bg='white')
        manage_frame.place(x=1137,y=50,width=210,height=400)
        l_id_pur = Label(manage_frame, text='الرقم عملية الشراء',bg='white')
        l_id_pur.pack()
        id_pur = Entry(manage_frame,textvariable=pur_id, bd='2', justify='center')
        id_pur.pack()
        l_name_pur = Label(manage_frame, text='إسم عملية الشراء',bg='white')
        l_name_pur.pack()
        name_pur = Entry(manage_frame, textvariable=pur_name, bd='2', justify='center')
        name_pur.pack()
        l_pur_purchase_amount = Label(manage_frame, text=' مبلغ الشراء',bg='white')
        l_pur_purchase_amount.pack()
        pur_purchase_amount = Entry(manage_frame, textvariable=pur_purchase_amount, bd='2', justify='center')
        pur_purchase_amount.pack()
        l_pur_date_purchase = Label(manage_frame, text='تاريخ الشراء',bg='white')
        l_pur_date_purchase.pack()
        pur_date_purchase = Entry(manage_frame,textvariable=pur_date_purchase, bd='2', justify='center')
        pur_date_purchase.pack()
        l_pur_type = Label(manage_frame, text=' نوع الشراء',bg='white')
        l_pur_type.pack()
        pur_type = ttk.Combobox(manage_frame, textvariable=pur_type, justify='center')
        pur_type['value']=('كاش','أجل')
        pur_type.pack()
        l_del_pur = Label(manage_frame, text=' حذف عملية شراء برقم',bg='white', fg='red')
        l_del_pur.place(x=50,y=300)
        del_pur = Entry(manage_frame, textvariable=delete_pur, bd='2', justify='center')
        del_pur.place(x=44,y=330)
        
        
                
        #----------------------- dietals عرض النتائج والبيانات ---------------------------------------------
        dietals_frame = Frame(pro,bg='#F2F4F4')
        dietals_frame.place(x=1,y=102,width=1138,height=605)
        
        #-------- scrollbar ------------------------
        scroll_x = Scrollbar(dietals_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(dietals_frame, orient=VERTICAL)
        
        #-------- treeveiw -------------------------
        purchase_table = ttk.Treeview(dietals_frame,
        columns=('pur_type','pur_date_purchase','pur_purchase_amount','pur_name','pur_id'),
        xscrollcommand = scroll_x.set,
        yscrollcommand = scroll_y.set)
        purchase_table.place(x=18,y=1,width=1130,height=587)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)
         #-------- scrollbar  إحتياط---------------------
        scroll_x.config(command=purchase_table.xview)
        scroll_y.config(command=purchase_table.yview)
        
        
        def get_cursor(ev):
                cursor_row = purchase_table.focus()
                contents = purchase_table.item(cursor_row)
                row = contents['values']    
                pur_type.set(row[0])     
                pur_date_purchase.set(row[1])     
                pur_purchase_amount.set(row[2])    
                pur_name.set(row[3])     
                pur_id.set(row[4]) 
        
        purchase_table['show']='headings'
        purchase_table.heading('pur_type',text=' نوع عملية الشراء')
        purchase_table.heading('pur_date_purchase',text='تاريخ الشراء')
        purchase_table.heading('pur_purchase_amount',text=' مبلغ الشراء')
        purchase_table.heading('pur_name',text='إسم عملية الشراء')
        purchase_table.heading('pur_id',text='رقم عملية الشراء')
        
        purchase_table.column('pur_type',width=125)
        purchase_table.column('pur_date_purchase',width=65)
        purchase_table.column('pur_purchase_amount',width=65)
        purchase_table.column('pur_name',width=150)
        purchase_table.column('pur_id',width=20)
        purchase_table.bind("<ButtonRelease-1>",get_cursor)
        
        
        #------------------- connect database + add --------------------------------------
        def fetch_all():
                        conn = pymysql.connect(
                                        host = 'localhost',
                                        user = 'safwan',
                                        password = 'safwan123',
                                        database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute('select * from purchase')
                        rows = cur.fetchall()
                        if len(rows) !=0:
                                purchase_table.delete(*purchase_table.get_children())
                                for row in rows:
                                        purchase_table.insert("",END,value=row)
                        
                                conn.commit()
                        conn.close()
        
        
        
        fetch_all()
        def add_purchase():
                        conn = pymysql.connect(
                                host = 'localhost',
                                user = 'safwan',
                                password = 'safwan123',
                                database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute("insert into purchase values(%s,%s,%s,%s,%s)",(     
                                                                        pur_type.get(),     
                                                                        pur_date_purchase.get(),     
                                                                        pur_purchase_amount.get(),     
                                                                        pur_name.get(),     
                                                                        pur_id.get()     
                                                                        ))
                        conn.commit()
                        clear()
                        fetch_all()
                        conn.close()
                        
                        
        def update_purchase():
                        conn = pymysql.connect(
                                host = 'localhost',
                                user = 'safwan',
                                password = 'safwan123',
                                database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute("update purchase set pur_type=%s , pur_date_purchase=%s, pur_purchase_amount=%s, pur_name=%s, pur_id=%s",(     
                                                                                                                        pur_type.get(),     
                                                                                                                        pur_date_purchase.get(),     
                                                                                                                        pur_purchase_amount.get(),     
                                                                                                                        pur_name.get(),     
                                                                                                                        pur_id.get()     
                                                                                                                        ))
                        conn.commit()
                        clear()
                        fetch_all()
                        conn.close()
                        
                        
                        
        def search_purchase():
                        conn = pymysql.connect(
                                        host = 'localhost',
                                        user = 'safwan',
                                        password = 'safwan123',
                                        database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute("select * from purchase where pur_" +
                        str(search_by.get())+" LIKE '%"+str(pur_search.get())+"%'")
                        rows = cur.fetchall()
                        if len(rows) !=0:
                                purchase_table.delete(*purchase_table.get_children())
                                for row in rows:
                                        purchase_table.insert("",END,value=row)
                        
                                conn.commit()
                        conn.close()
                        
                        
        def delete():
                        conn = pymysql.connect(
                                        host = 'localhost',
                                        user = 'safwan',
                                        password = 'safwan123',
                                        database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute('delete from purchase where pur_id=%s',delete_pur.get())
                        conn.commit()
                        fetch_all()
                        conn.close() 
                        
                                
        def clear():   
                        pur_type.set('')     
                        pur_date_purchase.set('')     
                        pur_purchase_amount.set('')    
                        pur_name.set('')     
                        pur_id.set('')
                        
                        
                        
        def about():
                messagebox.showinfo("devloper Safwan Saadan","welcome to our first project") 

#---------------------  buttons  الأزرار -------------------------
        btn_frame = Frame(pro,bg ='white')
        btn_frame.place(x=1137,y=435,width=210,height=353)
        titlel = Label(btn_frame,text='لوحة التحكم', font=('Deco',14),fg='red')
        titlel.pack(fill=X)
        
        add_btn=Button(btn_frame,text='إضافة عملية شراء',bg='green',fg='white', command=add_purchase)
        add_btn.place(x=33,y=33,width=150,height=30)
        del_btn=Button(btn_frame,text='حذف عملية شراء',bg='red',fg='white', command=delete)
        del_btn.place(x=33,y=66,width=150,height=30)
        update_btn=Button(btn_frame,text='تعديل بيانات عملية شراء',bg='#3498DB',fg='white', command=update_purchase)
        update_btn.place(x=33,y=99,width=150,height=30)
        clear_btn=Button(btn_frame,text='إفراغ الحقول',bg='#85929E',fg='white', command=clear)
        clear_btn.place(x=33,y=132,width=150,height=30)
        about_btn=Button(btn_frame,text='من نحن',bg='#85929E',fg='white', command=about)
        about_btn.place(x=33,y=165,width=150,height=30)
        exit_btn=Button(btn_frame,text='إغلاق البرنامج',bg='red',fg='white', command=pro.quit)
        exit_btn.place(x=33,y=198,width=150,height=30)
        
#---------------------- search manage البحث  -------------------------------------------
        search_frame = Frame(pro,bg='white')
        search_frame.place(x=1,y=50,width=1138,height=50)
        
        l_search = Label(search_frame,text='البحث عن عملية شراء', font=('Deco',14) , fg='red' , bg='white')
        l_search.place(x=990,y=12)
        
        combo_search = ttk.Combobox(search_frame, textvariable=search_by, justify='right')
        combo_search['value']=('id','name','purchase_amount','date_purchase','salary')
        combo_search.place(x=890,y=12,width=100,height=25)
        
        search_pur = Entry(search_frame, textvariable=pur_search, justify='right' , bd='2')
        search_pur.place(x=635,y=12,width=250,height=25)
        
        search_btn = Button(search_frame , text='بحث', bg='#3498DB', fg='white', command=search_purchase)
        search_btn.place(x=530,y=12,width=100,height=25)
        
        
        
        
        
        
        
#---------------------------------------------------- الموردون : suppliers ------------------------------------------
#---------------------------------------------------- الموردون : suppliers ------------------------------------------

def suppliers():
    #--------------- إنشاء نافذة البرنامج ------------------------
        
        title = Label(pro ,
        text='[ نظام إدارة الموردين]',
        bg='#1AAECB',
        font=('monospace',16),
        fg='white')
        title.pack(fill=X)

#-----------------------  varible  --------------------
        sup_id =StringVar()
        sup_name =StringVar()
        sup_phone =StringVar()
        sup_address =StringVar()
        delete_sup =StringVar()
        sup_search =StringVar()
        search_by =StringVar()
        
#--------------------------- أدوات التحكم بالبرنامج ------------------------------
        manage_frame = Frame(pro, bg='white')
        manage_frame.place(x=1137,y=50,width=210,height=400)
        l_id_sup = Label(manage_frame, text='الرقم التسلسي',bg='white')
        l_id_sup.pack()
        id_sup = Entry(manage_frame,textvariable=sup_id, bd='2', justify='center')
        id_sup.pack()
        l_name_sup = Label(manage_frame, text='إسم المورد',bg='white')
        l_name_sup.pack()
        name_sup = Entry(manage_frame, textvariable=sup_name, bd='2', justify='center')
        name_sup.pack()
        l_phone_sup = Label(manage_frame, text='رقم الهاتف',bg='white')
        l_phone_sup.pack()
        phone_sup = Entry(manage_frame,textvariable=sup_phone, bd='2', justify='center')
        phone_sup.pack()
        l_address_sup = Label(manage_frame, text=' العنوان',bg='white')
        l_address_sup.pack()
        address_sup = Entry(manage_frame, textvariable=sup_address, bd='2', justify='center')
        address_sup.pack()
        l_del_sup = Label(manage_frame, text=' حذف مورد بالرقم التسلسلي',bg='white', fg='red')
        l_del_sup.place(x=50,y=300)
        del_sup = Entry(manage_frame, textvariable=delete_sup, bd='2', justify='center')
        del_sup.place(x=44,y=330)
        
        
        #----------------------- dietals عرض النتائج والبيانات ---------------------------------------------
        dietals_frame = Frame(pro,bg='#F2F4F4')
        dietals_frame.place(x=1,y=102,width=1138,height=605)
        
        #-------- scrollbar ------------------------
        scroll_x = Scrollbar(dietals_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(dietals_frame, orient=VERTICAL)
        
        #-------- treeveiw -------------------------
        suppliers_table = ttk.Treeview(dietals_frame,
        columns=('sup_address','sup_phone','sup_name','sup_id'),
        xscrollcommand = scroll_x.set,
        yscrollcommand = scroll_y.set)
        suppliers_table.place(x=18,y=1,width=1130,height=587)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)
         #-------- scrollbar  إحتياط---------------------
        scroll_x.config(command=suppliers_table.xview)
        scroll_y.config(command=suppliers_table.yview)
        
        
        def get_cursor(ev):
                cursor_row = suppliers_table.focus()
                contents = suppliers_table.item(cursor_row)
                row = contents['values']   
                sup_address.set(row[0])     
                sup_phone.set(row[1])        
                sup_name.set(row[2])     
                sup_id.set(row[3]) 
        
        suppliers_table['show']='headings'
        suppliers_table.heading('sup_address',text=' العنوان')
        suppliers_table.heading('sup_phone',text='رقم الهاتف')
        suppliers_table.heading('sup_name',text='إسم العميل')
        suppliers_table.heading('sup_id',text='رقم العميل')
        
        suppliers_table.column('sup_address',width=125)
        suppliers_table.column('sup_phone',width=65)
        suppliers_table.column('sup_name',width=150)
        suppliers_table.column('sup_id',width=20)
        suppliers_table.bind("<ButtonRelease-1>",get_cursor)
        
        #------------------- connect database + add --------------------------------------
        def fetch_all():
                        conn = pymysql.connect(
                                        host = 'localhost',
                                        user = 'safwan',
                                        password = 'safwan123',
                                        database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute('select * from suppliers')
                        rows = cur.fetchall()
                        if len(rows) !=0:
                                suppliers_table.delete(*suppliers_table.get_children())
                                for row in rows:
                                        suppliers_table.insert("",END,value=row)
                        
                                conn.commit()
                        conn.close()
        
        fetch_all()
        def add_suppliers():
                        conn = pymysql.connect(
                                host = 'localhost',
                                user = 'safwan',
                                password = 'safwan123',
                                database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute("insert into suppliers values(%s,%s,%s,%s)",(     
                                                                        sup_address.get(),     
                                                                        sup_phone.get(),         
                                                                        sup_name.get(),     
                                                                        sup_id.get()     
                                                                        ))
                        conn.commit()
                        clear()
                        fetch_all()
                        conn.close()
                        
                        
        def update_suppliers():
                        conn = pymysql.connect(
                                host = 'localhost',
                                user = 'safwan',
                                password = 'safwan123',
                                database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute("update suppliers set sup_address=%s , sup_phone=%s, sup_name=%s, sup_id=%s",(     
                                                                                                sup_address.get(),     
                                                                                                sup_phone.get(),         
                                                                                                sup_name.get(),     
                                                                                                sup_id.get()     
                                                                                                ))
                        conn.commit()
                        clear()
                        fetch_all()
                        conn.close()
                        
                        
        
                        
                        
        def search_suppliers():
                        conn = pymysql.connect(
                                        host = 'localhost',
                                        user = 'safwan',
                                        password = 'safwan123',
                                        database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute("select * from suppliers where sup_" +
                        str(search_by.get())+" LIKE '%"+str(sup_search.get())+"%'")
                        rows = cur.fetchall()
                        if len(rows) !=0:
                                suppliers_table.delete(*suppliers_table.get_children())
                                for row in rows:
                                        suppliers_table.insert("",END,value=row)
                        
                                conn.commit()
                        conn.close()
                        
                        
        def delete():
                        conn = pymysql.connect(
                                        host = 'localhost',
                                        user = 'safwan',
                                        password = 'safwan123',
                                        database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute('delete from suppliers where sup_id=%s',delete_sup.get())
                        conn.commit()
                        fetch_all()
                        conn.close() 
                        
                                
        def clear():     
                        sup_address.set('')     
                        sup_phone.set('')       
                        sup_name.set('')     
                        sup_id.set('')
                        
                        
                        
        def about():
                messagebox.showinfo("devloper Safwan Saadan","welcome to our first project") 

#---------------------  buttons  الأزرار -------------------------
        btn_frame = Frame(pro,bg ='white')
        btn_frame.place(x=1137,y=435,width=210,height=353)
        titlel = Label(btn_frame,text='لوحة التحكم', font=('Deco',14),fg='red')
        titlel.pack(fill=X)
        
        add_btn=Button(btn_frame,text='إضافة مورد',bg='green',fg='white', command=add_suppliers)
        add_btn.place(x=33,y=33,width=150,height=30)
        del_btn=Button(btn_frame,text='حذف مورد',bg='red',fg='white', command=delete)
        del_btn.place(x=33,y=66,width=150,height=30)
        update_btn=Button(btn_frame,text='تعديل بيانات مورد',bg='#3498DB',fg='white', command=update_suppliers)
        update_btn.place(x=33,y=99,width=150,height=30)
        clear_btn=Button(btn_frame,text='إفراغ الحقول',bg='#85929E',fg='white', command=clear)
        clear_btn.place(x=33,y=132,width=150,height=30)
        about_btn=Button(btn_frame,text='من نحن',bg='#85929E',fg='white', command=about)
        about_btn.place(x=33,y=165,width=150,height=30)
        exit_btn=Button(btn_frame,text='إغلاق البرنامج',bg='red',fg='white', command=pro.quit)
        exit_btn.place(x=33,y=198,width=150,height=30)
        
#---------------------- search manage البحث  -------------------------------------------
        search_frame = Frame(pro,bg='white')
        search_frame.place(x=1,y=50,width=1134,height=50)
        
        l_search = Label(search_frame,text='البحث عن مورد', font=('Deco',14) , fg='red' , bg='white')
        l_search.place(x=1000,y=12)
        
        combo_search = ttk.Combobox(search_frame, textvariable=search_by, justify='right')
        combo_search['value']=('id','name','phone','address')
        combo_search.place(x=900,y=12,width=100,height=25)
        
        search_sup = Entry(search_frame, textvariable=sup_search, justify='right' , bd='2')
        search_sup.place(x=645,y=12,width=250,height=25)
        
        search_btn = Button(search_frame , text='بحث', bg='#3498DB', fg='white', command=search_suppliers)
        search_btn.place(x=540,y=12,width=100,height=25)
        
        
        
        


#---------------------------------------------------- السلع : commodities ------------------------------------------
#---------------------------------------------------- السلع : commodities ------------------------------------------

def commodities():
    #--------------- إنشاء نافذة البرنامج ------------------------
        
        title = Label(pro ,
        text='[ نظام إدارة السلع ]',
        bg='#1AAECB',
        font=('monospace',16),
        fg='white')
        title.pack(fill=X)
#-----------------------  varible  --------------------
        com_id =StringVar()
        com_name =StringVar()
        com_cost =StringVar()
        com_categorie =StringVar()
        delete_com =StringVar()
        com_search =StringVar()
        search_by =StringVar()
#--------------------------- أدوات التحكم بالبرنامج ------------------------------
        manage_frame = Frame(pro, bg='white')
        manage_frame.place(x=1137,y=50,width=210,height=400)
        l_id_com = Label(manage_frame, text='الرقم التسلسي لسلعة',bg='white')
        l_id_com.pack()
        id_com = Entry(manage_frame,textvariable=com_id, bd='2', justify='center')
        id_com.pack()
        l_name_com = Label(manage_frame, text='إسم السلعة',bg='white')
        l_name_com.pack()
        name_com = Entry(manage_frame, textvariable=com_name, bd='2', justify='center')
        name_com.pack()
        l_cost_com = Label(manage_frame, text='سعر السلعة',bg='white')
        l_cost_com.pack()
        cost_com = Entry(manage_frame,textvariable=com_cost, bd='2', justify='center')
        cost_com.pack()
        l_categorie_com = Label(manage_frame, text=' صنف السلعة',bg='white')
        l_categorie_com.pack()
        categorie_com = Entry(manage_frame, textvariable=com_categorie, bd='2', justify='center')
        categorie_com.pack()
        l_del_com = Label(manage_frame, text=' حذف سلعة برقم',bg='white', fg='red')
        l_del_com.place(x=50,y=300)
        del_com = Entry(manage_frame, textvariable=delete_com, bd='2', justify='center')
        del_com.place(x=44,y=330)
        
                
                
        #----------------------- dietals عرض النتائج والبيانات ---------------------------------------------
        dietals_frame = Frame(pro,bg='#F2F4F4')
        dietals_frame.place(x=1,y=102,width=1138,height=605)
        #-------- scrollbar ------------------------
        scroll_x = Scrollbar(dietals_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(dietals_frame, orient=VERTICAL)
        #-------- treeveiw -------------------------
        commodities_table = ttk.Treeview(dietals_frame,
        columns=('com_categorie','com_cost','com_name','com_id'),
        xscrollcommand = scroll_x.set,
        yscrollcommand = scroll_y.set)
        commodities_table.place(x=18,y=1,width=1130,height=587)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)
         #-------- scrollbar  إحتياط---------------------
        scroll_x.config(command=commodities_table.xview)
        scroll_y.config(command=commodities_table.yview)
        
        
        def get_cursor(ev):
                cursor_row = commodities_table.focus()
                contents = commodities_table.item(cursor_row)
                row = contents['values']   
                com_categorie.set(row[0])     
                com_cost.set(row[1])        
                com_name.set(row[2])     
                com_id.set(row[3])
                
                
        commodities_table['show']='headings'
        commodities_table.heading('com_categorie',text=' صنف السلعة')
        commodities_table.heading('com_cost',text='سعر السلعة')
        commodities_table.heading('com_name',text='إسم السلعة')
        commodities_table.heading('com_id',text='رقم السلعة')
        commodities_table.column('com_categorie',width=125)
        commodities_table.column('com_cost',width=65)
        commodities_table.column('com_name',width=150)
        commodities_table.column('com_id',width=20)
        commodities_table.bind("<ButtonRelease-1>",get_cursor) 
        
        
        #------------------- connect database + add --------------------------------------
        def fetch_all():
                        conn = pymysql.connect(
                                        host = 'localhost',
                                        user = 'safwan',
                                        password = 'safwan123',
                                        database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute('select * from commodities')
                        rows = cur.fetchall()
                        if len(rows) !=0:
                                commodities_table.delete(*commodities_table.get_children())
                                for row in rows:
                                        commodities_table.insert("",END,value=row)
                                conn.commit()
                        conn.close()
        
        
        
        fetch_all()
        def add_commodities():
                        conn = pymysql.connect(
                                host = 'localhost',
                                user = 'safwan',
                                password = 'safwan123',
                                database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute("insert into commodities values(%s,%s,%s,%s)",(     
                                                                        com_categorie.get(),     
                                                                        com_cost.get(),         
                                                                        com_name.get(),     
                                                                        com_id.get()     
                                                                        ))
                        conn.commit()
                        clear()
                        fetch_all()
                        conn.close()
                        
                        
        def update_commodities():
                        conn = pymysql.connect(
                                host = 'localhost',
                                user = 'safwan',
                                password = 'safwan123',
                                database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute("update commodities set com_categorie=%s , com_cost=%s, com_name=%s, com_id=%s",(     
                                                                                                com_categorie.get(),     
                                                                                                com_cost.get(),         
                                                                                                com_name.get(),     
                                                                                                com_id.get()     
                                                                                                ))
                        conn.commit()
                        clear()
                        fetch_all()
                        conn.close()
                        
                        
        
        def search_commodities():
                        conn = pymysql.connect(
                                        host = 'localhost',
                                        user = 'safwan',
                                        password = 'safwan123',
                                        database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute("select * from commodities where com_" +
                        str(search_by.get())+" LIKE '%"+str(com_search.get())+"%'")
                        rows = cur.fetchall()
                        if len(rows) !=0:
                                commodities_table.delete(*commodities_table.get_children())
                                for row in rows:
                                        commodities_table.insert("",END,value=row)
                                conn.commit()
                        conn.close()
                        
                        
                        
        def delete():
                        conn = pymysql.connect(
                                        host = 'localhost',
                                        user = 'safwan',
                                        password = 'safwan123',
                                        database = 'pro_db')
                        cur = conn.cursor()
                        cur.execute('delete from commodities where com_id=%s',delete_com.get())
                        conn.commit()
                        fetch_all()
                        conn.close()
                        
                        
                         
        def clear():     
                        com_categorie.set('')     
                        com_cost.set('')       
                        com_name.set('')     
                        com_id.set('')
                        
                        
        
        def about():
                messagebox.showinfo("devloper Safwan Saadan","welcome to our first project")
                
                
                
#---------------------  buttons  الأزرار -------------------------
        btn_frame = Frame(pro,bg ='white')
        btn_frame.place(x=1137,y=435,width=210,height=353)
        titlel = Label(btn_frame,text='لوحة التحكم', font=('Deco',14),fg='red')
        titlel.pack(fill=X)
        add_btn=Button(btn_frame,text='إضافة سلعة',bg='green',fg='white', command=add_commodities)
        add_btn.place(x=33,y=33,width=150,height=30)
        del_btn=Button(btn_frame,text='حذف سلعة',bg='red',fg='white', command=delete)
        del_btn.place(x=33,y=66,width=150,height=30)
        update_btn=Button(btn_frame,text='تعديل بيانات سلعة',bg='#3498DB',fg='white', command=update_commodities)
        update_btn.place(x=33,y=99,width=150,height=30)
        clear_btn=Button(btn_frame,text='إفراغ الحقول',bg='#85929E',fg='white', command=clear)
        clear_btn.place(x=33,y=132,width=150,height=30)
        about_btn=Button(btn_frame,text='من نحن',bg='#85929E',fg='white', command=about)
        about_btn.place(x=33,y=165,width=150,height=30)
        exit_btn=Button(btn_frame,text='إغلاق البرنامج',bg='red',fg='white', command=pro.quit)
        exit_btn.place(x=33,y=198,width=150,height=30)
        
        
#---------------------- search manage البحث  -------------------------------------------
        search_frame = Frame(pro,bg='white')
        search_frame.place(x=1,y=50,width=1134,height=50)
        l_search = Label(search_frame,text='البحث عن سلعة', font=('Deco',14) , fg='red' , bg='white')
        l_search.place(x=1000,y=12)
        combo_search = ttk.Combobox(search_frame, textvariable=search_by, justify='right')
        combo_search['value']=('id','name','cost','categorie')
        combo_search.place(x=900,y=12,width=100,height=25)
        search_com = Entry(search_frame, textvariable=com_search, justify='right' , bd='2')
        search_com.place(x=645,y=12,width=250,height=25)
        search_btn = Button(search_frame , text='بحث', bg='#3498DB', fg='white', command=search_commodities)
        search_btn.place(x=540,y=12,width=100,height=25)
        
        





#---------------------------------------------------- تسجيل الدخول : login ------------------------------------------
#---------------------------------------------------- تسجيل الدخول : login ------------------------------------------

def login():
        pro.config(background = '#D5DBDB')
        # pro.iconbitmap('')

        #---------------- title العنوان -----------------
        title =Label(pro, text='LOGIN SYSTEM',font=('Courier',15),bg='black',fg='white')
        title.pack(fill=X)

        #---------------- frame  ---------------------------
        frl = Frame(pro, width='300',height='450',bg='blue')
        frl.pack(pady=30)

        #---------------- image : الصور ---------------------
        # photo = PhotoImage(file="c:\\Users\\Safwan\\Desktop\\pro\\images\\logo.png")
        # panel = Label(frl, image=photo)
        # panel.place(x=1,y=1)

         #--------------- label ------------------------------
        
        lb1 = Label(frl,text='USERNAME : ',font=('Courier',15),bg='whitesmoke')
        lb1.place(x=10,y=140)
        lb2 = Label(frl,text='PASSWORD : ',font=('Courier',15),bg='whitesmoke')
        lb2.place(x=10,y=180)
        
        
        username =StringVar()
        password =StringVar()

        #------------------ Entry : حقول الإدخال -------------------------------
        en1 = Entry(frl ,textvariable=username)
        en1.place(x=130,y=140,width=160,height=28)
        en2 = Entry(frl ,textvariable=password)
        en2.place(x=130,y=180,width=160,height=28)
        
        
        def clear():     
                username.set('')     
                password.set('')       
                

        def add_user():
                conn = pymysql.connect(
                        host = 'localhost',
                        user = 'safwan',
                        password = 'safwan123',
                        database = 'pro_db')
                cur = conn.cursor()
                cur.execute("insert into users values(%s,%s)",(     
                                                        username.get(),     
                                                        password.get()))
                conn.commit()
                clear()
                conn.close()
                
        
        def search_login():
                conn = pymysql.connect(
                                host = 'localhost',
                                user = 'safwan',
                                password = 'safwan123',
                                database = 'pro_db')
                cur = conn.cursor()
                log =cur.execute('SELECT * FROM users WHERE user_name=%s AND password=%s ',(
                                                                username.get(),     
                                                                password.get()))
                
                conn.close()
                if log == False:
                        lb = Label(frl,text=' المستخدم غير موجود',font=('monospace',14),
                                        fg='red')
                        lb.place(x=80,y=320)
                                
                else:
                        main()
                        
                clear()
                                        
        
        
        def admin():
                if username.get() == 'safwan' and password.get() == 'safwan@123':
                        lb = Label(frl,text=' أدخل  اسم المستخدم وكلمة مرور ',font=('monospace',14),
                                        fg='green')
                        lb.place(x=60,y=320)
                        bt2 = Button(frl,text='إضافة مستخدم',font=('Courier',15),bg='green',width='10', command=add_user)
                        bt2.place(x=80,y=360,width=150)
                 
                else:
                        lb = Label(frl,text='خطأ في المستخدم \nأو أنه ليس لديك الصلاحيات لإنشاء حسابات\n أدخل اسم وكلمة مرور مستخدم النظام\n المسؤول ثم إضغط إنشاء',font=('monospace',14),
                                        fg='red')
                        lb.place(x=20,y=305)
                               
                clear()
             
                                   
                        

        #----------------- checkbox --------------------------------------------
        c1 = Checkbutton(frl,text='Forget password !',font=('Courier',15),bg='whitesmoke')
        c1.place(x=40,y=220)
        c2 = Label(frl,text='Devloped by Safwan Saadan @2023 ',font=('Courier',9),bg='whitesmoke')
        c2.place(x=46,y=420)

        #---------------- Button الأزرار ----------------------------------------
        
        bt1 = Button(frl,text='LOGIN',font=('Courier',15),bg='#76D7C4',width='10', command=search_login)
        bt1.place(x=15,y=260)
        bt2 = Button(frl,text='SIGNIN',font=('Courier',15),bg='#CD6155',width='10', command=admin)
        bt2.place(x=155,y=260)
        
        
        
        
        
#---------------------------------------------------- الصفحة الرئيسية : main ------------------------------------------
#---------------------------------------------------- الصفحة الرئيسية : main ------------------------------------------

def main():
    #--------------- إنشاء نافذة البرنامج ------------------------
        
        title = Label(pro ,
        text='[ الصفحة الرئيسية  ]',
        bg='#1AAECB',
        font=('monospace',16),
        fg='white')
        title.pack(fill=X)
        
        
        option_frame = Frame(pro,bg='blue')
        option_frame.place(x=1,y=1,width=1370, height=50)
        
        main_frame = Frame(pro)
        main_frame.place(x=1,y=50,width=1370, height=700)
        
        #---------------- image : الصور ---------------------
        photo = PhotoImage(file="c:\\Users\\Safwan\\Desktop\\pro\\images\\4.png")
        panel = Label(main_frame, image=photo)
        panel.place(x=1,y=1)

        
        
        home_btn = Button(option_frame,text='الموظفون',font=('Bold',15),
                          fg='white',bd=0,bg='blue',
                          command=employees)
        home_btn.place(x=1250,y=1)
        
        home_indicate = Label(option_frame , text='',bg='blue')
        home_indicate.place(x=1250,y=40,width=70,height=5)
        
        
        menu_btn = Button(option_frame,text='العملاء',font=('Bold',15),
                          fg='white',bd=0,bg='blue',
                          command=clients)
        menu_btn.place(x=1100,y=1)
        
        menu_indicate = Label(option_frame , text='',bg='blue')
        menu_indicate.place(x=1100,y=40,width=70,height=5)
        
        contact_btn = Button(option_frame,text='الموردون',font=('Bold',15),
                          fg='white',bd=0,bg='blue',
                          command=suppliers)
        contact_btn.place(x=950,y=1)
        
        contact_indicate = Label(option_frame , text='',bg='blue')
        contact_indicate.place(x=950,y=40,width=70,height=5)
        
        
        about_btn = Button(option_frame,text='المبيعات',font=('Bold',15),
                          fg='white',bd=0,bg='blue',
                          command=sale)
        about_btn.place(x=800,y=1)
        
        about_indicate = Label(option_frame , text='',bg='blue')
        about_indicate.place(x=800,y=40,width=70,height=5)
        
        about_btn = Button(option_frame,text='المشتريات',font=('Bold',15),
                          fg='white',bd=0,bg='blue',
                          command=purchase)
        about_btn.place(x=650,y=1)
        
        about_indicate = Label(option_frame , text='',bg='blue')
        about_indicate.place(x=650,y=40,width=70,height=5)
        
        about_btn = Button(option_frame,text='السلع',font=('Bold',15),
                          fg='white',bd=0,bg='blue',
                          command=commodities)
        about_btn.place(x=500,y=1)
        
        about_indicate = Label(option_frame , text='',bg='blue')
        about_indicate.place(x=500,y=40,width=70,height=5)
        
        about_btn = Button(option_frame,text='من نحن؟',font=('Bold',15),
                          fg='white',bd=0,bg='blue',
                          command=about)
        about_btn.place(x=350,y=1)
        
        about_indicate = Label(option_frame , text='',bg='blue')
        about_indicate.place(x=350,y=40,width=70,height=5)
        
        about_btn = Button(option_frame ,text=' إغلاق البرنامج',font=('Bold',15),
                          fg='white',bd=0,bg='blue',
                          command=pro.quit)
        about_btn.place(x=100,y=1)
        
        about_indicate = Label(option_frame , text='',bg='blue')
        about_indicate.place(x=100,y=40,width=70,height=5)












login()


pro.mainloop()

