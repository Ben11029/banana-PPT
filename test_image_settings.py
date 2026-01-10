"""
测试图片设置是否正确传递和使用
"""
import requests
import json

BASE_URL = "http://localhost:5000"

def test_create_project_with_image_settings():
    """测试创建项目时图片设置是否正确保存"""
    print("🧪 测试1: 创建项目并检查图片设置...")
    
    # 创建项目
    response = requests.post(f"{BASE_URL}/api/projects", json={
        "creation_type": "idea",
        "idea_prompt": "测试图片设置",
        "image_resolution": "4K",
        "image_aspect_ratio": "21:9"
    })
    
    if response.status_code != 201:
        print(f"❌ 创建项目失败: {response.status_code}")
        print(response.text)
        return None
    
    project_id = response.json()['data']['project_id']
    print(f"✅ 项目创建成功: {project_id}")
    
    # 获取项目详情
    response = requests.get(f"{BASE_URL}/api/projects/{project_id}")
    if response.status_code != 200:
        print(f"❌ 获取项目失败: {response.status_code}")
        return None
    
    project_data = response.json()['data']
    
    # 验证图片设置
    if project_data.get('image_resolution') == '4K':
        print("✅ 图片分辨率保存正确: 4K")
    else:
        print(f"❌ 图片分辨率错误: {project_data.get('image_resolution')}")
    
    if project_data.get('image_aspect_ratio') == '21:9':
        print("✅ 图片比例保存正确: 21:9")
    else:
        print(f"❌ 图片比例错误: {project_data.get('image_aspect_ratio')}")
    
    return project_id

def test_default_values():
    """测试默认值是否正确"""
    print("\n🧪 测试2: 创建项目不指定图片设置，检查默认值...")
    
    response = requests.post(f"{BASE_URL}/api/projects", json={
        "creation_type": "idea",
        "idea_prompt": "测试默认设置"
    })
    
    if response.status_code != 201:
        print(f"❌ 创建项目失败: {response.status_code}")
        return None
    
    project_id = response.json()['data']['project_id']
    print(f"✅ 项目创建成功: {project_id}")
    
    # 获取项目详情
    response = requests.get(f"{BASE_URL}/api/projects/{project_id}")
    project_data = response.json()['data']
    
    # 验证默认值
    if project_data.get('image_resolution') == '2K':
        print("✅ 默认分辨率正确: 2K")
    else:
        print(f"⚠️ 默认分辨率: {project_data.get('image_resolution')}")
    
    if project_data.get('image_aspect_ratio') == '16:9':
        print("✅ 默认比例正确: 16:9")
    else:
        print(f"⚠️ 默认比例: {project_data.get('image_aspect_ratio')}")
    
    return project_id

if __name__ == "__main__":
    print("=" * 60)
    print("图片设置传递测试")
    print("=" * 60)
    
    try:
        # 测试自定义设置
        project_id1 = test_create_project_with_image_settings()
        
        # 测试默认设置
        project_id2 = test_default_values()
        
        print("\n" + "=" * 60)
        print("✅ 所有测试完成！")
        print("=" * 60)
        
        if project_id1:
            print(f"\n创建的测试项目1: {project_id1}")
        if project_id2:
            print(f"创建的测试项目2: {project_id2}")
        
    except requests.exceptions.ConnectionError:
        print("❌ 无法连接到后端服务，请确保后端正在运行")
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
