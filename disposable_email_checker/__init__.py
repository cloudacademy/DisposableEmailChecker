import re


class DisposableEmailChecker(object):
    """
    Check if an email is from a disposable
    email service
    """
    
    def __init__(self,database_path):
        with open(database_path) as database_file:
            self._disposable_domains = [line.strip() for line in database_file if line.strip()]
    
    def chunk(self,l,n):
        return (l[i:i+n] for i in xrange(0, len(l), n))
    
    def is_disposable(self, email):
        for email_group in self.chunk(self._disposable_domains, 20):
            regex = "(.*" + ")|(.*".join(email_group) + ")"
            if re.match(regex, email, re.IGNORECASE):
                return True
    
        return False
