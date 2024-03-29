class Matrix 
{
    public:
        vector<vector<int>> a;

        Matrix() {}
        Matrix operator+(const Matrix &o) 
        {
            Matrix sum(*this);
            for (size_t i = 0; i < sum.a.size(); i++) 
            {
                for (size_t j = 0; j < sum.a[i].size(); j++) 
                {
                    sum.a[i][j] += o.a[i][j];
                }
            }
            return sum;
        }
};