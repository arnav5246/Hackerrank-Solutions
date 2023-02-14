        //Write your code here
       
        for(int i=1; i<n ; i++){
            for(int j=i; j>=1; j--){

                if(new BigDecimal(s[j]).compareTo(new BigDecimal(s[j-1]))>0){   
                    String temp = s[j];
                    s[j] = s[j-1];
                    s[j-1] = temp;
                    
                }else{
                    break;
                }
            }  
        }

