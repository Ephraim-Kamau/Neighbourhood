from django.test import TestCase
from .models import Posts, Profile, NeighbourHood, Businesses
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.epho = Profile(id = 10, full_name = "Ephraim Kamau", profile_pic = "", user_email = "kephraim19@gmail.com")

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.epho,Profile))
    
    def test_initialization(self):
        self.assertEqual(self.epho.full_name,"Ephraim Kamau")
        self.assertEqual(self.epho.profile_pic,"")
        self.assertEqual(self.epho.user_email, "kephraim19@gmail.com")

    # Testing Save method
    def test_create_profile(self):
        self.epho.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    # Testing Delete method
    def test_delete_profile(self):
        self.epho.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)



class NeighbourhoodTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.kasarani = NeighbourHood(id = 10, neighbourhood_name = "Kasarani", neighbourhood_location = "Nairobi",occupants_count = 2000)

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kasarani,NeighbourHood))
    
    def test_initialization(self):
        self.assertEqual(self.kasarani.neighbourhood_name,"Kasarani")
        self.assertEqual(self.kasarani.neighbourhood_location,"Nairobi")
        self.assertEqual(self.kasarani.occupants_count, 2000)
     

    # Testing Save method
    def test_create_neigborhood(self):
        self.kasarani.save_neighborhood()
        neighborhoods = NeighbourHood.objects.all()
        self.assertTrue(len(neighborhoods)>0)

    # Testing Delete method
    def test_delete_neigborhood(self):
        self.kasarani.delete_neighborhood()
        neighborhoods = NeighbourHood.objects.all()
        self.assertTrue(len(neighborhoods) == 0)


    
class PostsTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.epho = Profile(full_name = "Ephraim Kamau", profile_pic = "", user_email = "kephraim19@gmail.com")
        
        self.kasarani = NeighbourHood(neighbourhood_name = "Kasarani", neighbourhood_location = "Nairobi",occupants_count = 2000)
       
        self.posts = Posts(id = 10, title = "New Post", post = "This is a wonderful Post",pub_date = 16/4/2019)
    

        self.user = User(username="epho")

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.posts,Posts))

    def test_initialization(self):
        self.assertEqual(self.posts.title,"New Post")
        self.assertEqual(self.posts.post,"This is a wonderful Post")
        self.assertEqual(self.posts.pub_date, 16/4/2019)


    # Testing Delete method
    def test_delete_post(self):
        self.posts.delete_post()
        posts = Posts.objects.all()
        self.assertTrue(len(posts) == 0)


class BusinessesTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.grocer = Businesses(id = 10, business_name = "grocers", business_description = "A grocery business", business_email = "kephraim19@gmail.com")

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.grocer,Businesses))
    
    def test_initialization(self):
        self.assertEqual(self.grocer.business_name,"grocers")
        self.assertEqual(self.grocer.business_description,"A grocery business")
        self.assertEqual(self.grocer.business_email, "kephraim19@gmail.com")

    # Testing Save method
    def test_create_business(self):
        self.grocer.save_business()
        businesses = Businesses.objects.all()
        self.assertTrue(len(businesses)>0)

    # Testing Delete method
    def test_delete_business(self):
        self.grocer.delete_business()
        businesses = Businesses.objects.all()
        self.assertTrue(len(businesses) == 0)