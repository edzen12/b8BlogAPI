from rest_framework import serializers
from article.models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id','name','slug']
        read_only_fields = ['slug']


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Post
        fields = [
            'id','title','image','text','slug', 
            'category', 'category_id', 'created_at']
        read_only_fields = ['slug']