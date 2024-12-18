import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


# Example code to search for a specific product on Amazon using the Amazon Product Advertising API
def search_amazon_products(access_key, secret_key, associate_tag, keywords, region="us-east-1"):
    try:
        # Boto3를 이용해 클라이언트를 생성
        client = boto3.client(
            "advertising",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )

        # 상품 검색 요청
        response = client.search_items(
            PartnerTag=associate_tag,
            Keywords=keywords,
            SearchIndex="All",
            Resources=["Images.Primary.Small", "ItemInfo.Title", "Offers.Listings.Price"]
        )

        # 검색 결과 출력
        items = response.get("Items", [])
        if not items:
            print("검색 결과가 없습니다.")
        else:
            for item in items:
                title = item.get("ItemInfo", {}).get("Title", {}).get("DisplayValue", "제목 없음")
                price = item.get("Offers", {}).get("Listings", [])[0].get("Price", {}).get("DisplayAmount", "가격 정보 없음")
                print(f"상품명: {title}, 가격: {price}")

    except NoCredentialsError:
        print("AWS 자격 증명이 필요합니다.")
    except PartialCredentialsError:
        print("불완전한 자격 증명이 제공되었습니다.")
    except Exception as e:
        print(f"오류 발생: {str(e)}")


# 예시로 사용할 인증 정보 (실제 사용 시 자신의 Amazon Product Advertising API 키를 입력해야 합니다)
ACCESS_KEY = "YOUR_AMAZON_ACCESS_KEY"
SECRET_KEY = "YOUR_AMAZON_SECRET_KEY"
ASSOCIATE_TAG = "YOUR_AMAZON_ASSOCIATE_TAG"

# '노트북'이라는 키워드로 상품 검색
search_amazon_products(ACCESS_KEY, SECRET_KEY, ASSOCIATE_TAG, "노트북")