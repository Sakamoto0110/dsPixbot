def TryFindMemberIdByName(client,target):
    if not(target.startswith("@<") and target.endswith(">")):
        for member in client.members:
            if member.name == target or str(member.id) in target:
                return  member
    else:
        return None
            
def GetAuthorMentionString(msg):
    return "<@{0}>".format(msg.author.id)
    
def GetTargetMentionString(msg, target):
    return "<@{0}>".format(member.id) if (member := TryFindMemberIdByName(msg.guild,target)) != None else "the phantom *{0}*".format(target)