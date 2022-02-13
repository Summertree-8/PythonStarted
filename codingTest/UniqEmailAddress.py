class Solution:
    def numUniqueEmails(self, emails):
        result = set()
        for email in emails:
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.', '')
            result.add(local + '@' + domain)
        return len(result)