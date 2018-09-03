# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-20 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pecbyapi', '0005_auto_20180620_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='housespec',
            name='cooling_system',
            field=models.CharField(choices=[('RoomSpaceCooling', '居室部分にのみ冷房設備を設置する（居室のみを冷房する）'), ('AllSpaceCooling', '住戸全体（主居室、他居室、非居室の全て）を冷房する設備を設置する'), ('NotInstalled', '冷房設備を設置しない')], default='RoomSpaceCooling', help_text='一般的には「居室部分（主居室と他居室）にのみ冷房設備を設置する」を選択します。「住戸全体を冷房する設備を設置する」を選択すると、冷房設備は「ダクト式セントラル空調機」に設定されます。また、暖房設備も「ダクト式セントラル空調機」に設定されます。「冷房設備を設置しない」を選択した場合、「標準設備機器」を想定して一次エネルギー消費量が計算されます。', max_length=16, verbose_name='冷房方式の選択'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='heating_system',
            field=models.CharField(choices=[('RoomSpaceHeating', '居室部分にのみ暖房設備を設置する（居室のみを暖房する）'), ('AllSpaceHeating', '住戸全体（主居室、他居室、非居室の全て）を暖房する設備を設置する'), ('NotInstalled', '暖房設備を設置しない')], default='RoomSpaceHeating', help_text='一般的には「居室部分（主居室と他居室）にのみ暖房設備を設置する」を選択します。「住戸全体を暖房する設備を設置する」を選択すると、暖房設備は「ダクト式セントラル空調機」に設定されます。また、冷房設備も「ダクト式セントラル空調機」に設定されます。「暖房設備を設置しない」を選択した場合、「標準設備機器」を想定して一次エネルギー消費量が計算されます。', max_length=16, verbose_name='暖房方式の選択'),
        ),
        migrations.AlterField(
            model_name='housespec',
            name='ldk_cooling_type',
            field=models.CharField(choices=[('RoomAirConditioningCooling', 'エアコン'), ('OtherCoolingDevice', 'その他の冷房設備機器等')], default='RoomAirConditioningCooling', help_text='主居室の冷房設備を選択します。', max_length=36, verbose_name='主居室の冷房'),
        ),
        migrations.AlterField(
            model_name='housespec',
            name='ldk_heating_type',
            field=models.CharField(choices=[('RoomAirConditioningHeating', 'エアコン'), ('FFHeating', 'FF暖房機'), ('PanelRadiator', 'パネルラジエーター'), ('HotWaterFloorHeatingRadiator', '温水床暖房'), ('FanConvectorRadiator', 'ファンコンベクター'), ('ElecricFloorHeating', '電気ヒーター床暖房'), ('ElectricRoomHeaterWithThermalStorage', '電気蓄熱暖房器'), ('FloorHeatingWithRAC', 'エアコン付温水床暖房機'), ('OtherHeatingDevice', 'その他の暖房設備機器等')], default='RoomAirConditioningHeating', help_text='主居室の暖房設備を選択します。「エアコン」を選択すると、主居室の冷房設備も「エアコン」に設定されます。', max_length=36, verbose_name='主居室の暖房'),
        ),
        migrations.AlterField(
            model_name='housespec',
            name='oth_cooling_type',
            field=models.CharField(choices=[('RoomAirConditioningCooling', 'エアコン'), ('OtherCoolingDevice', 'その他の冷房設備機器等')], default='RoomAirConditioningCooling', help_text='他居室の冷房設備を選択します。', max_length=36, verbose_name='他居室の冷房'),
        ),
        migrations.AlterField(
            model_name='housespec',
            name='oth_heating_type',
            field=models.CharField(choices=[('RoomAirConditioningHeating', 'エアコン'), ('FFHeating', 'FF暖房機'), ('PanelRadiator', 'パネルラジエーター'), ('HotWaterFloorHeatingRadiator', '温水床暖房'), ('FanConvectorRadiator', 'ファンコンベクター'), ('ElecricFloorHeating', '電気ヒーター床暖房'), ('ElectricRoomHeaterWithThermalStorage', '電気蓄熱暖房器'), ('FloorHeatingWithRAC', 'エアコン付温水床暖房機'), ('OtherHeatingDevice', 'その他の暖房設備機器等')], default='RoomAirConditioningHeating', help_text='他居室の暖房設備を選択します。「エアコン」を選択すると、他居室の冷房設備も「エアコン」に設定されます。', max_length=36, verbose_name='他居室の暖房'),
        ),
    ]
