
class Amazon(object):
    """
    Fake Amazon API where we get customer data
    """
   def __init__(self, User_ID):
      self.User_ID = User_ID

   def getData(self):
     return [{"User_ID": self.User_ID, "field1": "test1", "field2":"test2", "Review": "Everything is good"}, {"User_ID": self.User_ID, "field1": "test1", "field2":"test2", "Review": "Bad Bad"}]

def clean_Amazon(json_data):
    """
    From messy data, we clean it to get just a list of text that can be used later
    """
    list_text = [d["Review"] for d in json_file]
    return list_text

def formatting(text, d=None):
    """
    Format text to IBM API format
    """
    api_format = {
         "content": text,
    }
    if d:
        api_format.update(d)
    return api_format

def generate_one_sample(list_text):
    for text in list_text:
        yield formatting(text)

def generate_all_samples_for_one_cust(list_text):
    list_content = list(generate_one_sample(list_text))
    json_file = {"contentItems": list_content}
    return json_file

def get_list_text_amazon(User_ID):
    json_file = Amazon(User_ID).getData()
    list_text = clean_Amazon(json_file)
    return generate_one_sample(list_text)
