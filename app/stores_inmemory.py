import itertools


class BaseStore():
    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self, item_instance):
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self._last_id += 1

    def get_by_id(self, id):
        result = None
        for item_instance in self._data_provider:
            if id == item_instance.id:
                result = item_instance
                break
        return result

    def update(self, instance):
        for index, instance_to_update in enumerate(self._data_provider):
            if instance.id == instance_to_update.id:
                self._data_provider[index] = instance
                break

    def delete(self, id):
        self._data_provider.remove(self.get_by_id(id))

    def entity_exists(self, instance):
        result = True
        if self.get_by_id(instance.id) is None:
            result = False
        return result


class MemberStore(BaseStore, object):
    members = []
    last_id = 1

    def __init__(self):
        super(MemberStore, self).__init__(MemberStore.members, MemberStore.last_id)

    def get_by_name(self, member_name):
        return (member for member in self.get_all() if member.name == member_name)

    def get_members_with_posts(self, all_posts):
        all_members = self.get_all()
        for member, post in itertools.product(all_members, all_posts):
            if member.id == post.member_id:
                member.posts.append(post)
        for member in all_members:
            yield member

    def get_top_two(self, all_posts):
        return sorted(self.get_members_with_posts(all_posts), key=lambda x: len(x.posts), reverse=True)[:2]


class PostStore(BaseStore, object):
    posts = []
    last_id = 1

    def __init__(self):
        super(PostStore, self).__init__(PostStore.posts, PostStore.last_id)

    def get_posts_by_date(self):
        return sorted(self.get_all(), key=lambda x: x.date, reverse=True)
