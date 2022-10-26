
def obj_to_post(obj, flag=True):
    post = dict(vars(obj))
    if obj.category:
        post['category'] = obj.category.name
    else:
        post['category'] = 'NoCategory'
    
    if obj.tags:
        post['tags'] = [tag.name for tag in obj.tags.all()]
    else:
        post['tags'] = []
        
    if obj.image:
        post['image'] = obj.image.url
    else:
        post['image'] = 'https://via.placeholder.com/900x400/'
        
    if obj.updated_at:
        post['updated_at'] = obj.updated_at.strftime('%y-%m-%d %H:%M:%S')
    else:
        post['updated_at'] = '9999-12-31 00:00:00'
    
    del post["_state"]
    if not flag:
        del post["category_id"]
        del post["created_at"]
        del post["content"]

    return post


def prev_next_post(obj):
    try:
        prevObj = obj.get_previous_by_updated_at()
        prevDict = {
            'id': prevObj.id,
            'title': prevObj.title,
        }
    except Exception as e:
        print(e)
        prevDict = {}
    
    try:
        nextObj = obj.get_next_by_updated_at()
        nextDict = {
            'id': nextObj.id,
            'title': nextObj.title,
        }
    except Exception as e:
        print(e)
        nextDict = {}
        
    return prevDict, nextDict