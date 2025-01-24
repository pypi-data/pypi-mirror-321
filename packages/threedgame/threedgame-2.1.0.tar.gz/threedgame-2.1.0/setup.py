from setuptools import setup, find_packages

setup(
    name='threedgame',
    version='2.1.0',
    packages=find_packages(),
    install_requires=[
        'ursina>=0.4.0',
    ],
    author='hhsdn',
    author_email='empiresoft@qq.com',
    description='A brief description of your library',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/feng/myfeng',  # 你的项目主页
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)