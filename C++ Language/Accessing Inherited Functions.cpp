class D : public A,B,C
{

    int val;
    public:
    D()
    {
        val = 1;
    }
    void update_val(int new_val)
    {
             int a = new_val;
             while(new_val!=0)
             {
                 if(val==a)
                    break;
                 if(new_val%2==0)
                 {
                     A::func(val);
                     new_val/=2;
                 }
                 else if(new_val%3==0)
                 {
                     B::func(val);
                     new_val/=3;
                 }
                 else if(new_val%5==0)
                 {
                     C::func(val);
                     new_val/=5;
                 }
             }
            
    }
    void check(int); 
};