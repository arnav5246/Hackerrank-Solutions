//Write your code here
static boolean flag;
static int B,H;

static{
    Scanner io = new Scanner(System.in);
    B = io.nextInt();
    H = io.nextInt();
    if(B>0 && H>0)
    {
        flag = true;
    }
    else
    {
        System.out.println("java.lang.Exception: Breadth and height must be positive");
    }
}
