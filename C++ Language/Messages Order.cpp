class Message 
{
    public: 
        Message() {}
        Message(const int& p_iID, const string& p_sText) : m_sText(p_sText), m_iID(p_iID) {}

        const string& get_text() 
        {
             return m_sText;   
        }
        const int& get_id() const {
            return m_iID;
        }
    private:
        string m_sText;
        int m_iID;

};

bool operator<(const Message& lhs, const Message& rhs) 
{
    return lhs.get_id() < rhs.get_id();
}

class MessageFactory 
{
    public:
        MessageFactory() {}
        Message create_message(const string& p_sText) 
        {
        return {m_iID++, p_sText};
        }
    private :
        int m_iID = 0;
};