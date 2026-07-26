class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split("@")

            idx = local.find("+")
            if idx != -1:
                local = local[:idx]
            
            local = local.replace(".", "")

            unique.add(f"{local}@{domain}")
        return len(unique)