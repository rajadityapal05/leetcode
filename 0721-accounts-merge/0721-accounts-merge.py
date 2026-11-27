
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = list(range(len(accounts)))
        rank = [0] * len(accounts)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

        email_to_id = {}

        # Connect accounts that share an email.
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_id:
                    union(i, email_to_id[email])
                else:
                    email_to_id[email] = i

        # Group emails by their connected account.
        merged = {}

        for email, account_id in email_to_id.items():
            root = find(account_id)
            if root not in merged:
                merged[root] = []
            merged[root].append(email)

        # Sort emails and add the account name.
        result = []

        for root, emails in merged.items():
            result.append([accounts[root][0]] + sorted(emails))

        return result
