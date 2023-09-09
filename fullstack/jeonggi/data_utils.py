import csv
from jeonggi.models import Jeonggi_Audition

def save_auditions_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # 첫 번째 행은 헤더이므로 건너뜁니다.
        for row in reader:
            audition_name = row[0]
            planning_agency = row[1]

            tmp1 = list(map(int, row[2].split(',')))  # ,을 기준으로 분할된 나이 리스트
            tmp2 = list(map(int, row[3].split(',')))
            if len(tmp1) >= 2:  # 시작 나이 조건이 2개 이상일 경우
                age_group1 = max(tmp1)
            else:
                age_group1 = tmp1[0]
            if len(tmp2) >= 2:  # 끝 나이 조건이 2개 이상일 경우
                age_group2 = max(tmp2)
            else:
                age_group2 = tmp2[0]
            recruitment_field = None if row[4] == "-" else row[4]
            gender = None if row[5] == "-" else row[5]
            due_date= "2099-12-30" if row[6] == "-" else row[6]
            url = None if row[8] == "-" else row[8]
            data_number = row[9]
            detail_data = row[7]
            img_url=row[10]
            
            # 데이터 모델 객체 생성 및 필드 값 할당
            jeonggi_audition_data = Jeonggi_Audition(
                planning_agency=planning_agency,
                audition_name=audition_name,
                recruitment_field=recruitment_field,
                age_group1=age_group1,
                age_group2=age_group2,
                gender=gender,
                due_date=due_date,
                url=url,
                data_number=data_number,
                detail_data=detail_data,
                img_url=img_url
            )
            
            # 객체 저장
            jeonggi_audition_data.save()
