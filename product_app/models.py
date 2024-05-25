from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):
    image = models.ImageField(upload_to='category-image', null=True, blank=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
   
    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ColorImage(models.Model):
    image = models.ImageField(upload_to='color', null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"ColorImage {self.id} - {self.name}"

class Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    images = models.ManyToManyField(ColorImage, related_name='colors')

    def __str__(self):
        return f"{self.product.name} - {self.name}"

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('product', 'size', 'color')

    def clean(self):
        # Ensure color is associated with the same product
        if self.color.product != self.product:
            raise ValidationError('The color must be associated with the same product as the product variant.')

    def save(self, *args, **kwargs):
        # Call clean method to perform validation before saving
        self.clean()
        super().save(*args, **kwargs)
        
        
    # def save(self, *args, **kwargs):
    #     if self.color.product != self.product:
    #         raise ValidationError('The color must be associated with the same product as the product variant.')
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.product.name} - {self.color.name} - {self.size.name}"
