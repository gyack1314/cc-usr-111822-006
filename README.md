# 机器人跨场景试验

项目按来源版本保存业务资料，已有 scenarios、outcomes、acceptance 环节。现有场景定义、试验结果与验收汇总只做场景内计数，尚未判定不同配置与人工接管下的泛化可比性。

运行与检查：

    python -m unittest discover -s tests -v
    python -m compileall -q robot_trial tests
    python -m robot_trial.cli data/example.json
