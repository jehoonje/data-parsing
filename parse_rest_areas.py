import json

def load_data(file_path):
    """
    JSON 파일을 읽어 데이터를 로드합니다.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"JSON 디코딩 오류: {e}")
        return []
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
        return []

def filter_fields(areas, fields):
    filtered_areas = []
    for area in areas:
        if isinstance(area, dict):  # area가 사전인지 확인
            filtered_area = {field: area.get(field, "") for field in fields}
            filtered_areas.append(filtered_area)
        else:
            print(f"Skipping non-dict object: {area}")
    return filtered_areas

def save_to_json(data, output_path):
    """
    필터링된 데이터를 JSON 파일로 저장합니다.
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print(f"데이터가 '{output_path}'에 저장되었습니다.")
    except Exception as e:
        print(f"파일 저장 중 오류 발생: {e}")

def main():
    # 입력 파일 경로
    input_file = 'rest_areas_raw.json'
    # 출력 파일 경로
    output_file = 'rest_areas_parsed.json'
    # 추출할 필드 목록
    fields_to_extract = [
        "휴게소명",
        "도로종류",
        "도로노선번호",
        "도로노선명",
        "도로노선방향",
        "위도",
        "경도",
        "휴게소종류",
        "주유소유무",
        "전기차충전소유무"
    ]

    # 데이터 로드
    rest_areas_data = load_data(input_file)

    if not rest_areas_data:
        print("데이터 로드에 실패했습니다.")
        return

    # 'records' 키의 데이터를 가져오기
    rest_areas = rest_areas_data.get("records", [])

    # 필드 필터링
    filtered_rest_areas = filter_fields(rest_areas, fields_to_extract)

    # 결과 저장
    save_to_json(filtered_rest_areas, output_file)

if __name__ == "__main__":
    main()
