import re


class DisposableEmailChecker(object):
    """
    Check if an email is from a disposable
    email service
    """
    
    def __init__(self,database_path):
        self.emails = [line.strip() for line in open(database_path)]
    
    def chunk(self,l,n):
        return (l[i:i+n] for i in xrange(0, len(l), n))
    
    def is_disposable(self, email):
        for email_group in self.chunk(self.emails, 20):
            regex = "(.*" + ")|(.*".join(email_group) + ")"
            if re.match(regex, email):
                return True
    
        return False
