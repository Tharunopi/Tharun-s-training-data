import cv2
import numpy as np
import random
from PIL import Image, ImageDraw, ImageFont
import os
import string

class CheckImageGenerator:
    def __init__(self, output_dir='check_images'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'legitimate'), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'fake'), exist_ok=True)

    def generate_random_name(self):
        """Generate a random realistic name"""
        first_names = [
            'John', 'Emma', 'Michael', 'Sophia', 'William', 'Olivia',
            'James', 'Ava', 'Alexander', 'Isabella', 'David', 'Mia',
            'Robert', 'Emily', 'Daniel', 'Madison', 'Matthew', 'Abigail'
        ]
        last_names = [
            'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia',
            'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Taylor', 'Harris'
        ]
        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def generate_bank_name(self):
        """Generate a random bank name"""
        bank_prefixes = ['National', 'United', 'First', 'Community', 'State']
        bank_types = ['Bank', 'Financial', 'Trust', 'Credit Union']
        return f"{random.choice(bank_prefixes)} {random.choice(bank_types)}"

    def generate_legitimate_check(self, index):
        """Generate a realistic legitimate check image"""
        img = Image.new('RGB', (800, 400), color='white')
        draw = ImageDraw.Draw(img)

        # Load a professional font
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()

        # Bank details
        bank_name = self.generate_bank_name()
        draw.text((50, 50), bank_name, fill='black', font=font)

        # Check number
        check_number = f"Check No: {random.randint(10000, 99999)}"
        draw.text((600, 50), check_number, fill='black', font=font)

        # Date
        date = f"Date: {random.randint(1, 12)}/{random.randint(1, 28)}/2024"
        draw.text((50, 100), date, fill='black', font=font)

        # Payee
        payee = self.generate_random_name()
        draw.text((50, 150), f"Pay to the order of: {payee}", fill='black', font=font)

        # Amount
        amount = f"$ {random.randint(100, 10000)}.{random.randint(10, 99)}"
        draw.text((50, 200), amount, fill='black', font=font)

        # Routing and account numbers
        routing_number = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        account_number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        draw.text((50, 250), f"Routing: {routing_number}", fill='black', font=font)
        draw.text((50, 300), f"Account: {account_number}", fill='black', font=font)

        # Signature placeholder
        draw.line([(50, 350), (250, 350)], fill='gray', width=2)
        draw.text((100, 370), "Signature", fill='gray', font=font)

        # Save image
        filepath = os.path.join(self.output_dir, 'legitimate', f'legitimate_check_{index}.png')
        img.save(filepath)
        return filepath

    def generate_fake_check(self, index):
        """Generate a synthetic fake check with deliberate anomalies"""
        img = Image.new('RGB', (800, 400), color='white')
        draw = ImageDraw.Draw(img)

        # Load a professional font
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()

        # Anomaly types with more detailed forgery techniques
        anomaly_types = [
            "Significant Amount Alteration",
            "Completely Forged Signature",
            "Mismatched Bank Information",
            "Duplicate Check Number",
            "Suspicious Endorsement"
        ]
        anomaly = random.choice(anomaly_types)

        # Apply specific fake check characteristics
        if anomaly == "Significant Amount Alteration":
            original_amount = f"$ {random.randint(100, 1000)}"
            altered_amount = f"$ {random.randint(50000, 500000)}"
            draw.text((50, 50), "AMOUNT ALTERED!", fill='red', font=font)
            draw.text((50, 150), f"Original: {original_amount}", fill='gray', font=font)
            draw.text((50, 200), f"Altered: {altered_amount}", fill='red', font=font)

        elif anomaly == "Completely Forged Signature":
            draw.text((50, 50), "FORGED SIGNATURE DETECTED", fill='red', font=font)
            # Create an unnatural signature
            for _ in range(5):
                x1, y1 = random.randint(50, 250), random.randint(300, 380)
                x2, y2 = random.randint(50, 250), random.randint(300, 380)
                draw.line([(x1, y1), (x2, y2)], fill='red', width=3)

        elif anomaly == "Mismatched Bank Information":
            fake_bank = ''.join(random.choices(string.ascii_uppercase, k=8)) + " Bank"
            draw.text((50, 50), f"SUSPICIOUS BANK: {fake_bank}", fill='red', font=font)
            draw.text((50, 100), "Inconsistent Bank Details", fill='red', font=font)

        elif anomaly == "Duplicate Check Number":
            duplicate_number = f"Check No: {random.randint(10000, 99999)}"
            draw.text((50, 50), "DUPLICATE CHECK NUMBER", fill='red', font=font)
            draw.text((50, 150), duplicate_number, fill='red', font=font)

        else:  # Suspicious Endorsement
            draw.text((50, 50), "SUSPICIOUS ENDORSEMENT", fill='red', font=font)
            fake_endorser = ''.join(random.choices(string.ascii_uppercase, k=10))
            draw.text((50, 150), f"Endorsement: {fake_endorser}", fill='red', font=font)

        # Save image
        filepath = os.path.join(self.output_dir, 'fake', f'fake_check_{index}.png')
        img.save(filepath)
        return filepath

    def generate_dataset(self, num_legitimate=100, num_fake=100):
        """Generate entire dataset"""
        legitimate_paths = []
        fake_paths = []

        # Generate legitimate checks
        for i in range(num_legitimate):
            path = self.generate_legitimate_check(i)
            legitimate_paths.append(path)

        # Generate fake checks
        for i in range(num_fake):
            path = self.generate_fake_check(i)
            fake_paths.append(path)

        return legitimate_paths, fake_paths

def main():
    generator = CheckImageGenerator()
    leg_paths, fake_paths = generator.generate_dataset()

    print(f"Generated {len(leg_paths)} Legitimate Checks")
    print(f"Generated {len(fake_paths)} Fake Checks")
    print("\nDataset Location: check_images/")

if __name__ == "__main__":
    main()