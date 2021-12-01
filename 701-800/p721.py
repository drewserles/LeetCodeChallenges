'''
First pass I created a hideous solution that works.

Learning opportunity from the solution: this can be modelled as a graph problem or a "union-find" aka "disjoint-set data structure".
I'll see if I can figure out how to do this as a graph, then learn about how to do a union find.

After some review I realized I'd seen disjoint sets in CSC263. This is an exercise is writing a functioning disjoint set data structure.
Important ideas here - go through and create my own union find and my own DFS.

It looks like the DFS solutions are significantly faster.
'''

class DJS:
    def __init__(self, sz):
        # Initialize the dataset with a fixed number of sets. They are initially all distinct and are their own representative
        self.root = [i for i in range(sz)] 
    
    def find(self, x):
        # Pass in a set representative (in this context, that's an email account index).
        # If this hasn't been merged with another set it will return the same value, if it has then the return will be the merged set representative
        while self.root[x] != x:
            x = self.root[x]
        return x
    
    def union(self, x, y):
        ''' 
        Input is the representative to two sets.
        To merge all we do is update the pointer to the representative, meaning the self.root data structure. So x's representative is now the rep for the 
        merged set, and y's rep points to x's rep.
        Should I point y's rep to x or to x's parent? Doesn't matter too much since this implementation isn't fast or anything
        '''
        x_r = self.find(x)
        y_r = self.find(y)
        self.root[y_r] = x_r


class Solution:
    '''
        1. Initialize DJS with length equal to len(accounts)
        2. Iterate through all the accounts, all their emails.
            Check if each email is in email_hash.
                If not this is a new email, add it with the current account idx #.
                If yes then we've seen this email before meaning the set of the existing email and this set should be merged. Note: pass the existing index first 
        3. Assembly time
            What's a good way to assemble into proper sets?
            Could iterate through the key,value in email_hash and maintain another hash with the index as the key and a list of emails as the value
        4. Get account name, sort, return
            Use the index from 3 to get the account name from accounts.
    '''
    def accountsMergeDJS(self, accounts):
        djs = DJS(len(accounts))
        email_hash = {}
        res_hash = {}

        for account_idx in range(len(accounts)):
            account = accounts[account_idx]
            for email_idx in range(1, len(account)):
                email = account[email_idx]
                # New email - map email to accounts idx
                if email not in email_hash:
                    email_hash[email] = account_idx
                # existing email - merge this account with the existing email's account
                else:
                    djs.union(email_hash[email], account_idx)
        
        # Get the index of the merged set for each email (stored value was the set index when it was entered, would have changed on a merge)
        for key,value in email_hash.items():
            merged_set_idx = djs.find(value)
            if merged_set_idx not in res_hash:
                res_hash[merged_set_idx] = [key]
            else:
                res_hash[merged_set_idx].append(key)
        # Create the result
        return [[accounts[key][0]] + sorted(value) for key,value in res_hash.items()]

    '''
        1. Build a graph - each account in accounts should be a connected component. Just connected enough to make it searchable
        2. When an email already exists we just connect those components, creating a merged connection
        3. Perform DFS on the Graph to find connected subcomponents.

        This could be made much nicer but I'm going to leave as is because it's instructional. Create a cleaner version below
    '''
    def accountsMergeDFS(self, accounts):
        def dfs(v,colour,graph):
            colour[v] = 1
            res = [v]
            for v_e in graph[v]:
                if colour[v_e] == 0:
                    res += dfs(v_e, colour, graph)
            return res

        email_to_num, num_to_email, counter = {}, {}, 0
        graph = []
        # Could simplify this by attaching each piece to the first node
        for account in accounts:
            for email_idx in range(1, len(account)):
                email, prev_email = account[email_idx], account[email_idx-1]
                # Haven't seen this email yet - add it to the dictionaries, connect it to the previous node
                if email not in email_to_num:
                    email_to_num[email] = counter
                    num_to_email[counter] = [account[0], email]
                    # Make connection between current and previous in graph
                    if email_idx > 1:
                        prev_num = email_to_num[prev_email]
                        graph.append([prev_num])
                        graph[prev_num].append(counter)
                    else:
                        graph.append([])
                    counter += 1
                # Have seen it - connect this component to the existing one
                else:
                    # Only need to do anything if there's an existing chain
                    if email_idx > 1:
                        num = email_to_num[email]
                        prev_num = email_to_num[prev_email]
                        graph[prev_num].append(num)
                        graph[num].append(prev_num)
        
        # Now do DFS
        colour = [0]*len(graph)
        components = []
        for v in range(len(colour)):
            if colour[v] == 0:
                components.append(dfs(v, colour, graph))
        return [[num_to_email[comp[0]][0]] + sorted([num_to_email[i][1] for i in comp]) for comp in components]

    '''
        Attempt at a cleaner version - using sets for the graphs and just connecting to the first email in the account rather than the previous one
    '''
    def accountsMergeDFS_V2(self, accounts):
            email_to_name, graph = {}, {}
            # Could simplify this by attaching each piece to the first node
            for account in accounts:
                name = account[0]
                ref_email = account[1]
                for email in account[1:]:
                    # Haven't seen this email yet - add it to the dictionaries, connect it to the previous node
                    if email not in graph:
                        graph[email] = set()
                    graph[email].add(ref_email)
                    graph[ref_email].add(email)
                    email_to_name[email] = name
            
            # Now do DFS
            seen, components = set(), []

            def dfs(email):
                seen.add(email)
                res = [email]
                for v_e in graph[email]:
                    if v_e not in seen:
                        res += dfs(v_e)
                return res

            for email in graph:
                if email not in seen:
                    components.append(dfs(email))
            return [[email_to_name[comp[0]]] + sorted(comp) for comp in components]
    '''
    What I came up with before I learned about union-find vs. DFS approaches.
    It works and does a somewhat similar thing to the union find but a bit uglier. Not terrible though
    '''
    def accountsMergeFirstAttempt(self, accounts):
        result, email_hash = [], {} #Email hash is email -> idx value
        curr_idx, valid_idxs = 0, []
        for acc in accounts:
            name, acc_emails = acc[0], acc[1:]
            seen_idxs, new_email_list = set(), set()
            for email in acc_emails:
                # Found overlap with an existing email, so this person already exists in the system.
                # Want to track these new emails and keep of track of index where they're saved
                if email in email_hash:
                    seen_idxs.add(email_hash[email])
                new_email_list.add(email)
            # retrieve the emails at each index and union them to the new email list. Remove the existing emails from valid
            for i in seen_idxs:
                new_email_list = new_email_list.union(result[i][1])
                valid_idxs.remove(i)
            # Iterate over all emails and update their index in email hash.
            for e in new_email_list:
                email_hash[e] = curr_idx
            # Then add result
            valid_idxs.append(curr_idx)
            result.append([name, new_email_list])
            curr_idx += 1
            
        return [[result[i][0]] + sorted(list(result[i][1])) for i in valid_idxs]

if __name__ == "__main__":
    sol = Solution()
    # accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
    print(sol.accountsMergeDFS_V2(accounts))