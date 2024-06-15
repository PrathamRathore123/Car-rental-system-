print(" \t\t      *       ********  **     *       *                             ")
print(" \t\t     * *      *      *  * *    *      * *                            ")
print(" \t\t    *   *     ********  *  *   *     *   *                           ")
print(" \t\t   *******    *         *   *  *    *******                          ")
print(" \t\t  *       *   *         *    * *   *       *                         ")
print(" \t\t *         *  *         *     **  *         *                        ")   
print("                                                                          ")
print("  *********        *        ********        *        *********  ********* ")
print("  *               * *       *      *       * *       *          *         ")
print("  *              *   *      ********      *   *      *          *         ")
print("  *  ******     *******     **           *******     *  ******  ********* ")
print("  *       *    *       *    *  *        *       *    *       *  *         ")
print("  *       *   *         *   *    *     *         *   *       *  *         ")
print("  *********  *           *  *      *  *           *  *********  ********* ")



A=input("Enter Your Name:  ")


class ApnaGarage:
    def __init__(self,stock):
        self.stock=stock
    def displaycar(self):
        print("Total cars in Stock" , self.stock)

        print("\t *****************************************************************************************************")
        print("\t * NO.*   CAR BRAND     *    CAR NAME    * REGISTRATION NO. *     CHASSIS NO    *      PRICE/DAY     *")
        print("\t *****************************************************************************************************")
        print("\t * 01 *   Ferrari      *   La Ferrari    *    MH01OO0007    * 1HGCM82633A123456 *      1000/-        *")
        print("\t * 02 *   Audi         *   Q8            *    MH02AA4444    * 2FGCM82633A123456 *      1000/-        *")
        print("\t * 03 *   BMW          *   720D          *    MH03CA0001    * 3GGCM82633A123456 *      1000/-        *")
        print("\t * 04 *   Bentley      *   Bentayga      *    DL02NB0007    * 4RGCM82633A123456 *      1000/-        *")
        print("\t * 05 *   Aston Martin *   DB12          *    DL02GT0009    * 5JGCM82633A123456 *      1000/-        *")
        print("\t * 06 *   Honda        *   Elevate       *    MP43CA5643    * 6TGCM82633A123456 *      1000/-        *")
        print("\t * 07 *   Ford         *   Endeavour     *    MP43CA1976    * 7JGCM82633A123456 *      1000/-        *")
        print("\t * 08 *   Toyota       *   Fortuner      *    MP43BD8976    * 8YGCM82633A123456 *      1000/-        *")
        print("\t * 09 *   MG           *   Gloster       *    MP43BH0934    * 9TGCM82633A123456 *      1000/-        *")
        print("\t * 10 *   Kia          *   Seltos        *    MP43IN0478    * 0IGCM82633A123456 *      1000/-        *")
        print("\t *****************************************************************************************************")
      

    
    def rentforcar(self,q):
        if q<=0:
            print("Enter the positine value or greater then zero")
        elif q>self.stock:
            print("Enter the value less then stock")
        else:
            self.stock=self.stock-q
            print("Total price",q*1000)
            print("Total cars remain in Stock",self.stock)
            
while True:
    obj=ApnaGarage(10)
    uc=int(input('''
    1 Total Cars      
    2 Exit
    '''))
    if uc==1:
        obj.displaycar()
        n=int(input("Select Car:  "))
        q=int(input("Enter the Qty:  "))
        d=int(input("Enter the No. of Days:  "))
        print("Total Price = ",((1000*d)*q))
        i=(input("Print Invoice:  "))
             
        if n==1:   
            print("Car_Brand = Ferrari")
            print("Car Name = La Ferrari")
            print("Registration No. = MH01OO0007")
            print("Chassis No. = 1HGCM82633A123456")
            print("Price =",1000*d)
            Car='dict1'
        elif n==2:
            print("Car Brand = Audi")
            print("Car Name = Q8")
            print("Registration No. = MH02AA4444")
            print("Chassis No. = 2FGCM82633A123456")
            print("Price =",1000*d)
            Car='dict2'
        elif n==3:
            print("Car Brand = BMW")
            print("Car Name = 720D")
            print("Registration No. = MH03CA0001")
            print("Chassis No. = 3GGCM82633A123456")
            print("Price =",1000*d)
            Car='dict3'

        elif n==4:
            print("Car Brand = Bentley")
            print("Car Name = Bentayga")
            print("Registration No. = DL02NB0007")
            print("Chassis No. = 4RGCM82633A123456")
            print("Price =",1000*d)
            Car='dict4'
        elif n==5:
            print("Car Brand = Aston Martin")
            print("Car Name = DB12")
            print("Registration No. = DL02GT0009")
            print("Chassis No. = 5JGCM82633A123456")
            print("Price =",1000*d)
            Car='dict5'
        elif n==6:
            print("Car Brand = Honda")
            print("Car Name = Elevate")
            print("Registration No. = MP43CA5643")
            print("Chassis No. = 6TGCM82633A123456")
            print("Price =",1000*d)
            Car='dict6'
        elif n==7:
            print("Car Brand = Ford")
            print("Car Name = Endeavour")
            print("Registration No. = MP43CA1976")
            print("Chassis No. = 7JGCM82633A123456")
            print("Price =",1000*d)
            Car='dict7'
        elif n==8:
            print("Car Brand = Toyota")
            print("Car Name = Fortuner")
            print("Registration No. = MP43BD8976")
            print("Chassis No. = 8YGCM82633A123456")
            print("Price =",1000*d)
            Car='dict8'
        elif n==9:
            print("Car Brand = MG")
            print("Car Name = Gloster")
            print("Registration No. = MP43BH0934")
            print("Chassis No. = 9TGCM82633A123456")
            print("Price =",1000*d)
            Car='dict9'
        elif n==10:
            print("Car Brand = Kia")
            print("Car Name = Seltos")
            print("Registration No. = MP43IN0478")
            print("Chassis No. = 0IGCM82633A123456")
            print("Price =",1000*d)
            Car='dict10'

        cars={
        'dict1':{'Car_Brand':'Ferrari','Car_Name':'La Ferrari','Registration No.':'MH01OO0007'},
        'dict2':{'Car_Brand':'Audi','Car_Name':'Q8','Registration No.':'MH02AA4444'},
        'dict3':{'Car_Brand':'BMW','Car_Name':'720D','Registration No.':'MH03CA0001'},
        'dict4':{'Car_Brand':'Bentley','Car_Name':'Bentayga','Registration No.':'DL02NB0007'},
        'dict5':{'Car_Brand':'Aston Martin','Car_Name':'DB12','Registration No.':'DL02GT0009'},
        'dict6':{'Car_Brand':'Honda','Car_Name':'Elevate','Registration No.':'MP43CA5643'},
        'dict7':{'Car_Brand':'Ford','Car_Name':'Endevour','Registration No.':'MP43CA1976'},
        'dict8':{'Car_Brand':'Toyota','Car_Name':'Fortuner','Registration No.':'MP43BD8976'},
        'dict9':{'Car_Brand':'MG','Car_Name':'Gloster','Registration No.':'MP43BH0934'},
        'dict10':{'Car_Name':'Kia','Car_Name':'Seltos','Registration No.':'MP43IN0478'},}
        
        s_id=cars[Car]
        print("\t\t\t**********************************************")
        print("\t\t\t                 CAR RENTAL                   ")
        print("\t\t\t**********************************************")
        print("\t\t\t    Invoice No.       *  042023001           ")
        print("\t\t\t    Customer Name     *",A,"                    ")
        print("\t\t\t    Car Brand         *",f'{s_id["Car_Brand"]}',"              ")
        print("\t\t\t    Car Name          *",f'{s_id["Car_Name"]}',"           ")
        print("\t\t\t    Registration no.  *",f'{s_id["Registration No."]}',"           ")
        print("\t\t\t    No. of days       *",d,"                    ")
        print("\t\t\t    Qty of Car        *",q,"                    ")
        print("\t\t\t**********************************************")
        print("\t\t\t    Total Price       *",((1000*d))*q,"                ")
        print("\t\t\t**********************************************")


    
                           


    # elif uc==2:
        
    #     obj.rentforcar(n)
        
        print("")
        print("")
        print("")
        print("\t\t\t\t\tThank You!")    

    else:
        break

