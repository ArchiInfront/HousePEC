from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

import sys
from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create your models here.


########
######## HouseBuilder
########
class HouseBuilder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField('会社名', max_length=200, default='○○工務店', help_text='会社名を入力してください（最大100字）')

    def get_registered_houses(self):
        return HouseBasic.objects.filter(builder=self).count()

    def get_date_joined(self):
        return self.user.date_joined

    def get_builder_name(self):
        return self.name

    def get_absolute_url(self):
        return reverse('house_list', args=[str(self.id)])
    
    def __str__(self):
        return self.user.username


########
######## HouseBasic
########
class HouseBasic(models.Model):
    builder = models.ForeignKey(HouseBuilder, on_delete=models.CASCADE, related_name='houses')
    #builder = models.CharField('会社名', max_length=200, default=self.user.builder)
    name = models.CharField('住宅名', max_length=200, default="○○○○邸", help_text="住宅名を入力してください（最大100字）")
    create_date = models.DateTimeField('住宅登録日時', auto_now_add=True)
    update_date = models.DateTimeField('住宅更新日時', auto_now=True)

    REGION_LIST = (
        ('1', '1地域'),
        ('2', '2地域'),
        ('3', '3地域'),
        ('4', '4地域'),
        ('5', '5地域'),
        ('6', '6地域'),
        ('7', '7地域'),
        ('8', '8地域'),
    )
    region = models.CharField(
        '建設地域', max_length=1, choices=REGION_LIST, blank=False, default="2", 
        help_text="省エネルギー基準地域区分（1～8）を指定してください。")
    
    ANNUALSOLARLEVEL_LIST = (
        ('A1', 'A1区分(年間の日射量が特に少ない地域)'),
        ('A2', 'A2区分(年間の日射量が少ない地域)'),
        ('A3', 'A3区分(年間の日射量が中程度の地域)'),
        ('A4', 'A4区分(年間の日射量が多い地域)'),
        ('A5', 'A5区分(年間の日射量が特に多い地域)'),
    )
    annual_solar_level = models.CharField(
        '日射地域区分', max_length=2, choices=ANNUALSOLARLEVEL_LIST, blank=False, default="A2", 
        help_text="年間日射地域区分（A1～A5）を指定してください。")
    
    HEATSTORAGE_LIST = (
        ('HeatStorage', '利用する'),
        ('None', '利用しない'),
    )
    heat_storage = models.CharField(
        '蓄熱利用', max_length=11, choices=HEATSTORAGE_LIST, blank=False, default="None", 
        help_text="蓄熱利用の有無を指定してください。")

    UNDERFLOORVENTILATION_LIST = (
        ('AlwaysOn', '通年利用する'),
        ('None', '利用しない'),
    )
    under_floor_ventilation = models.CharField(
        '床下経由換気の採用', max_length=8, choices=UNDERFLOORVENTILATION_LIST, blank=False, default="None", 
        help_text="床下換気システム利用の有無を指定してください。")
    under_floor_ventilation_area_rate = models.IntegerField(
        '床下経由換気の面積割合[%]', default=0, blank=False, 
        help_text="外気が経由する床下の面積の割合を％(1～100までの整数)で入力してください。")

    NATURALWIND_LIST = (
        ('0', '自然風を利用しない'),
        ('5', '自然風を利用する（換気回数5回/h相当以上）'),
        ('20', '自然風を利用する（換気回数20回/h相当以上）'),
    )
    ldk_natural_wind = models.CharField(
        '主居室の通風利用', max_length=2, choices=NATURALWIND_LIST, blank=False, default="0", 
        help_text="主居室の自然風による1時間あたりの換気回数を指定してください。")
    oth_natural_wind = models.CharField(
        '他居室の通風利用', max_length=2, choices=NATURALWIND_LIST, blank=False, default="0", 
        help_text="他居室の自然風による1時間あたりの換気回数を指定してください。")

    total_area = models.DecimalField(
        '延床面積[m2]', max_digits=5, decimal_places=2, default=120.08, 
        help_text="延床面積（主居室、他居室、非居室の合計）を、小数点以下2桁まで入力して下さい。")
    ldk_area = models.DecimalField(
        '主居室床面積[m2]', max_digits=5, decimal_places=2, default=29.81, 
        help_text="主居室の床面積を、小数点以下2桁まで入力して下さい。")
    oth_area = models.DecimalField(
        '他居室床面積[m2]', max_digits=5, decimal_places=2, default=51.34, 
        help_text="他居室の床面積を、小数点以下2桁まで入力して下さい。")

    total_envelope_area = models.DecimalField(
        '外皮面積の合計[m2]', max_digits=5, decimal_places=2, default=307.51, 
        help_text="天井、外壁、床、開口部等、すべての外皮面積の合計を、小数点以下2桁まで入力して下さい。")
    ua_value = models.DecimalField(
        'UA値[W/m2・K]', max_digits=3, decimal_places=2, default=0.87, 
        help_text="外皮平均熱貫流率(UA値)を、小数点以下2桁まで入力して下さい。")
    winter_ha_value = models.DecimalField(
        '暖房期ηAH値[-]', max_digits=2, decimal_places=1, default=4.3, 
        help_text="暖房期平均日射熱取得率(ηAH値)を、小数点以下1桁まで入力して下さい。")
    summer_ha_value = models.DecimalField(
        '冷房期ηAC値[-]', max_digits=2, decimal_places=1, default=2.8, 
        help_text="冷房期平均日射熱取得率(ηAC値)を、小数点以下1桁まで入力して下さい。")

    #def get_builder_name(self):
    #    return self.user.builder

    def get_registered_specs(self):
        return HouseSpec.objects.filter(house=self).count()

    def nonldk_area_check(self):
        nonldk_area = self.total_area - (self.ldk_area + self.oth_area)
        if nonldk_area >= 0:
            return True
        return False
    
    def get_last_updated(self):
        return HouseSpec.objects.filter(house=self).order_by('-update_date').first()

    def get_absolute_url(self):
        return reverse('house_list', args=[str(self.id)])

    def __str__(self):
        return self.name


########
######## HouseSpec
########
class HouseSpec(models.Model):
    builder = models.ForeignKey(HouseBuilder, on_delete=models.CASCADE, related_name='specs')
    house = models.ForeignKey(HouseBasic, on_delete=models.CASCADE, related_name='specs')
    def get_registered_specs(self):
        return self.house.get_registered_specs()
    serial_no = models.IntegerField('設備仕様No.', default=0)
    update_date = models.DateTimeField('設備仕様更新日時', auto_now=True)
    calc_done = models.BooleanField('一次エネルギー消費量計算済み', default=False)
    resErrMessage = models.CharField(max_length=255, blank=True, default='')
    resE_T = models.FloatField(blank=True, default=0)
    resE_L = models.FloatField(blank=True, default=0)
    resE_W = models.FloatField(blank=True, default=0)
    resE_V = models.FloatField(blank=True, default=0)
    resE_C = models.FloatField(blank=True, default=0)
    resE_H = models.FloatField(blank=True, default=0)
    resE_M = models.FloatField(blank=True, default=0)
    resE_ST = models.FloatField(blank=True, default=0)
    resE_SL = models.FloatField(blank=True, default=0)
    resE_SW = models.FloatField(blank=True, default=0)
    resE_SV = models.FloatField(blank=True, default=0)
    resE_SC = models.FloatField(blank=True, default=0)
    resE_SH = models.FloatField(blank=True, default=0)
    resE_SM = models.FloatField(blank=True, default=0)
    resReduceByPV = models.FloatField(blank=True, default=0)
    resSellByPV = models.FloatField(blank=True, default=0)
    resGenerateByPV = models.FloatField(blank=True, default=0)
    resGenerateByCG = models.FloatField(blank=True, default=0)

    #暖房方式
    HEATING_SYSTEM_LIST = (
        ('RoomSpaceHeating', '居室部分にのみ暖房設備を設置する（居室のみを暖房する）'),
        ('AllSpaceHeating', '住戸全体（主居室、他居室、非居室の全て）を暖房する設備を設置する'),
        ('NotInstalled', '暖房設備を設置しない'),
        )
    heating_system = models.CharField(
        '暖房方式の選択', max_length=16, choices=HEATING_SYSTEM_LIST, blank=False, default="RoomSpaceHeating", 
        help_text="一般的には「居室部分（主居室と他居室）にのみ暖房設備を設置する」を選択します。「住戸全体を暖房する設備を設置する」を選択すると、暖房設備は「ダクト式セントラル空調機」に設定され、同時に冷房設備も「ダクト式セントラル空調機」に設定されます。「暖房設備を設置しない」を選択した場合、「標準設備機器」を想定して一次エネルギー消費量が計算されます。")
    #LDK_HEATING_TYPE_LIST = (
    #    ('RoomAirConditioningHeating', 'エアコン'),
    #    ('FFHeating', 'FF暖房機'),
    #    ('PanelRadiator', 'パネルラジエーター'),
    #    ('HotWaterFloorHeatingRadiator', '温水床暖房'),
    #    ('FanConvectorRadiator', 'ファンコンベクター'),
    #    ('ElecricFloorHeating', '電気ヒーター床暖房'),
    #    ('ElectricRoomHeaterWithThermalStorage', '電気蓄熱暖房器'),
    #    ('FloorHeatingWithRAC', 'エアコン付温水床暖房機'),
    #    #('ElectricHeatPumpCentralHeating', 'ダクト式セントラル空調機'),
    #    ('OtherHeatingDevice', 'その他の暖房設備機器等'),
    #    #('NotInstalled', '暖房設備機器または放熱器を設置しない'),
    #)
    HEATING_TYPE_LIST = (
        ('RoomAirConditioningHeating', 'エアコン'),
        ('FFHeating', 'FF暖房機'),
        ('PanelRadiator', 'パネルラジエーター'),
        ('HotWaterFloorHeatingRadiator', '温水床暖房'),
        ('FanConvectorRadiator', 'ファンコンベクター'),
        ('ElecricFloorHeating', '電気ヒーター床暖房'),
        ('ElectricRoomHeaterWithThermalStorage', '電気蓄熱暖房器'),
        ('FloorHeatingWithRAC', 'エアコン付温水床暖房機'),
        ('OtherHeatingDevice', 'その他の暖房設備機器等'),
        ('NotInstalled', '暖房設備機器または放熱器を設置しない'),
    )
    ldk_heating_type = models.CharField(
        '主居室の暖房', max_length=36, choices=HEATING_TYPE_LIST, blank=False, default="RoomAirConditioningHeating", 
        help_text="主居室の暖房設備を選択します。「エアコン」を選択すると、主居室の冷房設備も「エアコン」に設定されます。")
    oth_heating_type = models.CharField(
        '他居室の暖房', max_length=36, choices=HEATING_TYPE_LIST, blank=False, default="RoomAirConditioningHeating", 
        help_text="他居室の暖房設備を選択します。「エアコン」を選択すると、他居室の冷房設備も「エアコン」に設定されます。")

    #主居室
    #ルームエアコンディショナー
    AC_HEATING_EFFICIENCY_LIST = (
        ('I', '（い）エアコン'),
        ('RO', '（ろ）エアコン'),
        ('HA', '（は）エアコン'),
        ('None', 'エネルギー消費効率区分を指定しない')
    )
    AC_HEATING_COMPRESSOR_LIST = (
        ('Single', '搭載しない'),
        ('Variable', '搭載する'),
    )
    ldk_ac_heating_efficiency = models.CharField(
        'エネルギー消費効率区分：主居室', max_length=4, choices=AC_HEATING_EFFICIENCY_LIST, default="I", 
        help_text="主居室ルームエアコンディショナー暖房のエネルギー消費効率区分を指定します。")
    ldk_ac_heating_compressor = models.CharField(
        '容量可変型コンプレッサー：主居室', max_length=8, choices=AC_HEATING_COMPRESSOR_LIST, default="Single", 
        help_text="主居室ルームエアコンディショナーの容量可変型コンプレッサー搭載の有無を指定します。")
    #FF暖房機
    ldk_ff_saving_input = models.BooleanField(
        '主居室FF暖房のエネルギー消費効率の入力', default=True, 
        help_text="主居室FF暖房のエネルギー消費効率を入力する場合はチェックして下さい。")
    ldk_ff_heating_efficiency = models.DecimalField(
        'FF暖房効率[%]：主居室', max_digits=3, decimal_places=1, default=86.0, 
        help_text="主居室FF暖房機の定格能力におけるエネルギー消費効率を、小数点以下1桁まで指定します。")
    #パネルラジエーター
    #温水床暖房
    ldk_hotwater_floorheating_area_rate = models.DecimalField(
        '温水床暖敷設率[%]：主居室', max_digits=3, decimal_places=1, default=80, help_text="主居室温水床暖房の敷設率を、小数点以下1桁まで指定します。")
    ldk_hotwater_floorheating_upward_heatflow_rate = models.DecimalField(
        '温水床暖上面放熱率[%]：主居室', max_digits=2, decimal_places=0, default=90, help_text="主居室温水床暖房の上面放熱率を整数で指定します。")
    #ファンコンベクター
    #電気ヒーター床暖房
    ldk_elecric_floorheating_area_rate = models.DecimalField(
        '電気床暖敷設率[%]：主居室', max_digits=3, decimal_places=1, default=80, help_text="主居室電気ヒーター床暖房の敷設率を、小数点以下1桁まで指定します。")
    ldk_elecric_floorheating_upward_heatflow_rate = models.DecimalField(
        '電気床暖上面放熱率[%]：主居室', max_digits=2, decimal_places=0, default=90, help_text="主居室電気ヒーター床暖房の上面放熱率を整数で指定します。")
    #電気蓄熱暖房器
    #ルームエアコンディショナー付温水床暖房機
    AC_FLOORHEATING_PIPE_LIST = (
        ('Normal', '断熱配管を採用しない'),
        ('Insulated', '断熱配管を採用する'),
    )
    ldk_ac_floorheating_area_rate = models.DecimalField(
        'エアコン床暖敷設率[%]：主居室', max_digits=3, decimal_places=1, default=80, 
        help_text="主居室におけるルームエアコンディショナー付温水床暖房の敷設率を、小数点以下1桁まで指定します。")
    ldk_ac_floorheating_upward_heatflow_rate = models.DecimalField(
        'エアコン床暖上面放熱率[%]：主居室', max_digits=2, decimal_places=0, default=90, 
        help_text="主居室におけるルームエアコンディショナー付温水床暖房の上面放熱率を整数で指定します。")
    ldk_ac_floorheating_pipe = models.CharField(
        'エアコン床暖配管：主居室', max_length=9, choices=AC_FLOORHEATING_PIPE_LIST, default="Insulated", 
        help_text="主居室におけるルームエアコンディショナー付温水床暖房機の配管の断熱を選択します。")
    #その他の暖房設備機器等
    ldk_other_heating_device_name = models.CharField(
        'その他の暖房機器：主居室', max_length=200, default="薪ストーブ", help_text="主居室におけるその他の暖房設備機器名を入力してください（最大100字）")

    #他居室
    #ルームエアコンディショナー
    oth_ac_heating_efficiency = models.CharField(
        'エネルギー消費効率区分：他居室', max_length=4, choices=AC_HEATING_EFFICIENCY_LIST, default="I", 
        help_text="他居室ルームエアコンディショナー暖房のエネルギー消費効率区分を指定します。")

    oth_ac_heating_compressor = models.CharField(
        '容量可変型コンプレッサー：他居室', max_length=8, choices=AC_HEATING_COMPRESSOR_LIST, default="Single", 
        help_text="他居室ルームエアコンディショナーの容量可変型コンプレッサー搭載の有無を指定します。")
    #FF暖房機
    oth_ff_saving_input = models.BooleanField(
        '他居室FF暖房のエネルギー消費効率の入力', default=True, 
        help_text="他居室FF暖房のエネルギー消費効率を入力する場合はチェックして下さい。")
    oth_ff_heating_efficiency = models.DecimalField(
        'FF暖房効率[%]：他居室', max_digits=3, decimal_places=1, default=86.0, 
        help_text="他居室FF暖房機の定格能力におけるエネルギー消費効率を、小数点以下1桁まで指定します。")
    #パネルラジエーター
    #温水床暖房
    oth_hotwater_floorheating_area_rate = models.DecimalField(
        '温水床暖敷設率[%]：他居室', max_digits=3, decimal_places=1, default=80, help_text="他居室温水床暖房の敷設率を、小数点以下1桁まで指定します。")
    oth_hotwater_floorheating_upward_heatflow_rate = models.DecimalField(
        '温水床暖上面放熱率[%]：他居室', max_digits=2, decimal_places=0, default=90, help_text="他居室温水床暖房の上面放熱率を整数で指定します。")
    #ファンコンベクター
    #電気ヒーター床暖房
    oth_elecric_floorheating_area_rate = models.DecimalField(
        '電気床暖敷設率[%]：他居室', max_digits=3, decimal_places=1, default=80, help_text="他居室電気ヒーター床暖房の敷設率を、小数点以下1桁まで指定します。")
    oth_elecric_floorheating_upward_heatflow_rate = models.DecimalField(
        '電気床暖上面放熱率[%]：他居室', max_digits=2, decimal_places=0, default=90, help_text="他居室電気ヒーター床暖房の上面放熱率を整数で指定します。")
    #電気蓄熱暖房器
    #ルームエアコンディショナー付温水床暖房機
    oth_ac_floorheating_area_rate = models.DecimalField(
        'エアコン床暖敷設率[%]：他居室', max_digits=3, decimal_places=1, default=80, 
        help_text="他居室におけるルームエアコンディショナー付温水床暖房の敷設率を、小数点以下1桁まで指定します。")
    oth_ac_floorheating_upward_heatflow_rate = models.DecimalField(
        'エアコン床暖上面放熱率[%]：他居室', max_digits=2, decimal_places=0, default=90, 
        help_text="他居室におけるルームエアコンディショナー付温水床暖房の上面放熱率を整数で指定します。")
    oth_ac_floorheating_pipe = models.CharField(
        'エアコン床暖配管：他居室', max_length=9, choices=AC_FLOORHEATING_PIPE_LIST, default="Insulated", 
        help_text="他居室におけるルームエアコンディショナー付温水床暖房機の配管の断熱を選択します。")
    #その他の暖房設備機器等
    oth_other_heating_device_name = models.CharField(
        'その他の暖房機器：他居室', max_length=200, default="薪ストーブ", help_text="他居室におけるその他の暖房設備機器名を入力してください（最大100字）")

    #温水暖房熱源
    HOTWATER_HEATING_SYSTEM_LIST = (
        ('NonIntegrated', '温水暖房専用型'),
        ('Integrated', '給湯・温水暖房一体型'),
        ('Cogeneration', 'コージェネレーション'),
        ('Other', 'その他の温水暖房機'),
        ('NotUsed', '設置しない'),
    )
    hotwater_heating_system = models.CharField(
        '温水暖房熱源システム', max_length=13, choices=HOTWATER_HEATING_SYSTEM_LIST, blank=False, default="NonIntegrated", 
        help_text="温水暖房熱源システムを選択してください。")
    HOTWATER_HEATING_SOURCE_TYPE_LIST = (
        ('OilClassic', '石油従来型温水暖房機'),
        ('OilLatentHeatRecovery', '石油潜熱回収型温水暖房機'),
        ('GasClassic', 'ガス従来型温水暖房機'),
        ('GasLatentHeatRecovery', 'ガス潜熱回収型温水暖房機'),
        ('ElectricHeatPump', '電気ヒートポンプ式温水暖房機(フロン系冷媒)'),
        ('ElectricHeater', '電気ヒーター式温水暖房機'),
    )
    hotwater_heating_source_type = models.CharField(
        '温水暖房専用型熱源機器', max_length=21, choices=HOTWATER_HEATING_SOURCE_TYPE_LIST, blank=False, default="OilLatentHeatRecovery", 
        help_text="温水暖房専用型熱源機器を選択してください。")

    hotwater_heating_source_saving_input = models.BooleanField(
        '温水暖房熱源機のJIS効率の入力', default=True, 
        help_text="石油熱源機、ガス従来型熱源機、ガス潜熱回収型熱源機のJIS効率（定格能力におけるエネルギー消費効率）を入力する場合はチェックして下さい。")
    hotwater_heating_source_efficiency_OilClassic = models.DecimalField(
        '温水暖房熱源機（石油熱源機）JIS効率[%]', max_digits=3, decimal_places=1, default=82.0, 
        help_text="温水暖房熱源機（石油熱源機）のJIS効率（定格能力におけるエネルギー消費効率）を、小数点以下1桁まで入力します。")
    hotwater_heating_source_efficiency_GasClassic = models.DecimalField(
        '温水暖房熱源機（ガス従来型熱源機）JIS効率[%]', max_digits=3, decimal_places=1, default=81.0, 
        help_text="温水暖房熱源機（ガス従来型熱源機）のJIS効率（定格能力におけるエネルギー消費効率）を、小数点以下1桁まで入力します。")
    hotwater_heating_source_efficiency_GasLatentHeatRecovery = models.DecimalField(
        '温水暖房熱源機（ガス潜熱回収型熱源機）JIS効率[%]', max_digits=3, decimal_places=1, default=87.0, 
        help_text="温水暖房熱源機（ガス潜熱回収型熱源機）のJIS効率（定格能力におけるエネルギー消費効率）を、小数点以下1桁まで入力します。")
    hotwater_heating_source_name = models.CharField(
        'その他の温水暖房機', max_length=200, blank=True, help_text="その他の温水暖房機の名称を入力してください（最大100字）")

    HOTWATER_HEATING_SOURCE_PIPE_LIST = (
        ('Normal, AllInsulatedCompartment', '配管を断熱しない（配管は全て断熱区画内）'),
        ('Normal, NotAllInsulatedCompartment', '配管を断熱しない（全てもしくは一部の配管が断熱区画外にある）'),
        ('Insulated, AllInsulatedCompartment', '配管を断熱する（配管は全て断熱区画内）'),
        ('Insulated, NotAllInsulatedCompartment', '配管を断熱する（全てもしくは一部の配管が断熱区画外にある）'),
    )
    hotwater_heating_source_pipe = models.CharField(
        '温水暖房配管の断熱', max_length=47, choices=HOTWATER_HEATING_SOURCE_PIPE_LIST, default="Insulated, AllInsulatedCompartment", 
        help_text="温水暖房機配管の断熱を選択します。")

    #ダクト式セントラル空調機 暖房
    heating_rated_input = models.BooleanField(
        '定格暖房能力および定格暖房消費電力の入力', default=False, 
        help_text="定格暖房能力および定格暖房消費電力を入力する場合はチェックして下さい。")
    heating_rated_capacity = models.IntegerField(
        '定格暖房能力[W]', default=8000, blank=True, help_text="定格暖房能力[W]を整数で指定します。")
    heating_rated_power = models.IntegerField(
        '定格暖房消費電力[W]', default=2128, blank=True, help_text="定格暖房消費電力[W]を整数で指定します。")
    HEATING_POWER_CORRECTION_LIST = (
        ('Correct', '風量補正あり'),
        ('None', '風量補正なし'),
    )
    heating_power_correction = models.CharField(
        '風量補正の有無', max_length=7, choices=HEATING_POWER_CORRECTION_LIST, default="None", 
        help_text="ダクト式セントラル空調機の風量補正の有無を指定します。")
    heating_coefficient = models.DecimalField(
        '消費電力補正係数[-]', max_digits=3, decimal_places=2, default=1.65, 
        help_text="ダクト式セントラル空調機の消費電力補正係数[-]を、小数点以下2桁まで指定します。")

    #冷房方式
    COOLING_SYSTEM_LIST = (
        ('RoomSpaceCooling', '居室部分にのみ冷房設備を設置する（居室のみを冷房する）'),
        ('AllSpaceCooling', '住戸全体（主居室、他居室、非居室の全て）を冷房する設備を設置する'),
        ('NotInstalled', '冷房設備を設置しない'),
        )
    cooling_system = models.CharField(
        '冷房方式の選択', max_length=16, choices=COOLING_SYSTEM_LIST, blank=False, default="RoomSpaceCooling", 
        help_text="一般的には「居室部分（主居室と他居室）にのみ冷房設備を設置する」を選択します。「住戸全体を冷房する設備を設置する」を選択すると、冷房設備は「ダクト式セントラル空調機」に設定され、同時に暖房設備も「ダクト式セントラル空調機」に設定されます。「冷房設備を設置しない」を選択した場合、「標準設備機器」を想定して一次エネルギー消費量が計算されます。")
    #LDK_COOLING_TYPE_LIST = (
    #    ('RoomAirConditioningCooling', 'エアコン'),
    #    ('OtherCoolingDevice', 'その他の冷房設備機器等'),
    #    ('ElectricHeatPumpCentralCooling', 'ダクト式セントラル空調機'),
    #    ('NotInstalled', '冷房設備機器を設置しない'),
    #)
    COOLING_TYPE_LIST = (
        ('RoomAirConditioningCooling', 'エアコン'),
        ('OtherCoolingDevice', 'その他の冷房設備機器等'),
        ('NotInstalled', '冷房設備機器を設置しない'),
    )
    ldk_cooling_type = models.CharField(
        '主居室の冷房', max_length=36, choices=COOLING_TYPE_LIST, blank=False, default="RoomAirConditioningCooling", 
        help_text="主居室の冷房設備を選択します。")
    oth_cooling_type = models.CharField(
        '他居室の冷房', max_length=36, choices=COOLING_TYPE_LIST, blank=False, default="RoomAirConditioningCooling", 
        help_text="他居室の冷房設備を選択します。")

    #ルームエアコンディショナー
    AC_COOLING_EFFICIENCY_LIST = (
        ('I', '（い）エアコン'),
        ('RO', '（ろ）エアコン'),
        ('HA', '（は）エアコン'),
        ('None', 'エネルギー消費効率区分を指定しない')
    )
    ldk_ac_cooling_efficiency = models.CharField(
        'エネルギー消費効率区分：主居室', max_length=2, choices=AC_COOLING_EFFICIENCY_LIST, default="I", 
        help_text="主居室におけるルームエアコンディショナー冷房のエネルギー消費効率の区分を指定します。")
    oth_ac_cooling_efficiency = models.CharField(
        'エネルギー消費効率区分：他居室', max_length=2, choices=AC_COOLING_EFFICIENCY_LIST, default="I", 
        help_text="他居室におけるルームエアコンディショナー冷房のエネルギー消費効率の区分を指定します。")

    AC_COOLING_COMPRESSOR_LIST = (
        ('Single', '搭載しない'),
        ('Variable', '搭載する'),
    )
    ldk_ac_cooling_compressor = models.CharField(
        '容量可変型コンプレッサー：主居室', max_length=8, choices=AC_COOLING_COMPRESSOR_LIST, default="Single", 
        help_text="主居室ルームエアコンディショナーの容量可変型コンプレッサー搭載の有無を指定します。")
    oth_ac_cooling_compressor = models.CharField(
        '容量可変型コンプレッサー：他居室', max_length=8, choices=AC_COOLING_COMPRESSOR_LIST, default="Single", 
        help_text="他居室ルームエアコンディショナーの容量可変型コンプレッサー搭載の有無を指定します。")

    #その他の冷房設備機器等
    ldk_other_cooling_device_name = models.CharField(
        'その他の冷房機器：主居室', max_length=200, default="扇風機", help_text="主居室におけるその他の冷房設備機器名を入力してください（最大100字）")
    oth_other_cooling_device_name = models.CharField(
        'その他の冷房機器：他居室', max_length=200, default="扇風機", help_text="他居室におけるその他の冷房設備機器名を入力してください（最大100字）")

    #ダクト式セントラル空調機 冷房
    cooling_rated_input = models.BooleanField(
        '定格冷房能力および定格冷房消費電力の入力', default=False, 
        help_text="定格冷房能力および定格冷房消費電力を入力する場合はチェックして下さい。")
    cooling_rated_capacity = models.IntegerField(
        '定格冷房能力[W]', default=7100, blank=True, help_text="定格冷房能力[W]を整数で指定します。")
    cooling_rated_power = models.IntegerField(
        '定格冷房消費電力[W]', default=2240, blank=True, help_text="定格冷房消費電力[W]を整数で指定します。")
    COOLING_POWER_CORRECTION_LIST = (
        ('Correct', '風量補正あり'),
        ('None', '風量補正なし'),
    )
    cooling_power_correction = models.CharField(
        '風量補正の有無', max_length=7, choices=COOLING_POWER_CORRECTION_LIST, default="None", 
        help_text="ダクト式セントラル空調機の風量補正の有無を指定します。")
    cooling_coefficient = models.DecimalField(
        '消費電力補正係数[-]', max_digits=3, decimal_places=2, default=1.69, 
        help_text="ダクト式セントラル空調機の消費電力補正係数[-]を、小数点以下2桁まで指定します。")

    #換気設備
    VENTILATION_TYPE_LIST = (
        ('DuctVenitlation1', 'ダクト式第1種換気設備'),
        ('DuctVentilation2or3', 'ダクト式第2種またはダクト式第3種換気設備'),
        ('WallMount1', '壁付け式第1種換気設備'),
        ('WallMount2or3', '壁付け式第2種換気設備または壁付け式第3種換気設備'),
    )
    ventilation_type = models.CharField(
        '換気設備', max_length=19, choices=VENTILATION_TYPE_LIST, blank=False, default="DuctVentilation2or3", 
        help_text="機械換気設備の種類を選択して下さい。")

    VENTILATION_SAVING_LIST = (
        ('ThickDuctOnly', '径の太いダクトを使用する'),
        ('ThickDuctAndDCMotor', '径の太いダクトを使用し、かつDCモーターを採用する'),
        ('SFP', '比消費電力を入力する'),
        ('None', '省エネルギー対策を指定しない')
    )
    ventilation_saving = models.CharField(
        '換気設備の省エネ手法', max_length=19, choices=VENTILATION_SAVING_LIST, blank=False, default="ThickDuctAndDCMotor", 
        help_text="採用する省エネルギー手法（径の太いダクト、DCモーター）を選択するか、あるいは比消費電力で評価する場合は「比消費電力を入力する」を選択します。")

    ventilation_sfp = models.DecimalField(
        '比消費電力[W/(m3/h)]', max_digits=4, decimal_places=2, default=0.30, 
        help_text="換気設備の比消費電力を、小数点以下2桁まで入力します。")

    VENTILATION_HEATEXCHANGER_LIST = (
        ('HeatExchanger', '熱交換換気を採用する'),
        ('None', '熱交換換気を採用しない'),
    )
    ventilation_heatexchanger = models.CharField(
        '熱交換換気', max_length=13, choices=VENTILATION_HEATEXCHANGER_LIST, blank=False, default="None", help_text="熱交換型換気の有無を選択します。")

    VENTILATION_FREQUENCY_LIST = (
        ('HalfPerHour', '0.5回/h'),
        ('ZeroPointSavenPerHour', '0.7回/h'),
        ('Zero', '0回/h'),
    )
    ventilation_frequency = models.CharField(
        '換気回数[回/h]', max_length=21, choices=VENTILATION_FREQUENCY_LIST, blank=False, default="HalfPerHour", help_text="通常は「0.5回/h」を選択します。")

    ventilation_efficiency = models.DecimalField(
        '有効換気量率[-]', max_digits=3, decimal_places=2, default=0.95, help_text="第1種換気設備の場合における有効換気量率を、小数点以下2桁まで入力します。")

    ventilation_heatexchanger_efficiency = models.DecimalField(
        '温度交換効率[%]', max_digits=2, decimal_places=0, default=65, help_text="熱交換換気の温度交換効率を40～95の範囲で入力します。")

    ventilation_heatexchanger_bal = models.DecimalField(
        '給気と排気の比率による温度交換効率の補正係数[-]', max_digits=3, decimal_places=2, default=0.90, 
        help_text="小数点以下2桁で入力します。補正係数の計算を行わない場合は0.90としてください。")

    ventilation_heatexchanger_leak = models.DecimalField(
        '排気過多時における住宅外皮経由の漏気による温度交換効率の補正係数[-]', max_digits=3, decimal_places=2, default=1, 
        help_text="小数点以下2桁で入力します。補正係数の計算を行わない場合は1.00としてください。")

    #給湯設備
    BATHROOM_LIST = (
        ('TapAndBath', '給湯蛇口と浴室がある'),
        ('TapOnly', '給湯蛇口がある（浴室無し）'),
        ('NA', '給湯設備無し'),
    )
    bathroom = models.CharField(
        '給湯蛇口・浴室の有無', max_length=12, choices=BATHROOM_LIST, blank=False, default="TapAndBath", 
        help_text="浴室やシャワー室等の有無を選択して下さい。浴室等も含め、台所や洗面にも給湯設備がない場合には、「給湯設備無し」を選択して下さい。")

    BATH_FUNCTION_LIST = (
        ('SingleFunction', '給湯単機能'),
        ('BathNoReheating', 'ふろ給湯器(追い焚きなし)'),
        ('BathReheating', 'ふろ給湯器(追い焚きあり)'),
    )
    bath_function = models.CharField(
        'ふろ機能の種類', max_length=15, choices=BATH_FUNCTION_LIST, default="BathReheating", help_text="ふろ機能の種類を選択します。")

    WATER_HEATER_TYPE_LIST = (
        ('GasClassic', 'ガス従来型給湯機（給湯専用型）'),
        ('GasLatentHeatRecovery', 'ガス潜熱回収型給湯機（給湯専用型）'),
        ('OilClassic', '石油従来型給湯機（給湯専用型）'),
        ('OilLatentHeatRecovery', '石油潜熱回収型給湯機（給湯専用型）'),
        ('ElectricHeater', '電気ヒーター式給湯機（給湯専用型）'),
        ('ElectricHeatPump', 'CO2冷媒電気ヒートポンプ給湯機（給湯専用型）'),
        ('Hybrid', '電気ヒートポンプ・ガス併用型給湯機（給湯専用型）'),
        ('Cogeneration', 'コージェネレーション'),
        ('Other', 'その他の給湯設備機器'),
        ('NotUsed', '給湯熱源機を設置しない'),
    )
    water_heater_type = models.CharField(
        '給湯熱源種類（給湯専用型）', max_length=31, choices=WATER_HEATER_TYPE_LIST, blank=False, default="ElectricHeatPump", 
        help_text="給湯熱源機の種類を選択して下さい。「給湯設備機器を設置しない」を選択した場合、「標準設備機器」を想定して一次エネルギー消費量が計算されます。")
   
    INTEGRATED_WATER_HEATER_TYPE_LIST = (
        ('IntegratedGasClassic', 'ガス従来型給湯温水暖房機（給湯・温水暖房一体型）'),
        ('IntegratedGasLatentHeatRecovery', 'ガス潜熱回収型給湯温水暖房機（給湯・温水暖房一体型）'),
        ('IntegratedOil', '石油従来型給湯温水暖房機（給湯・温水暖房一体型）'),
        ('IntegratedOilLatentHeatRecovery', '石油潜熱回収型給湯温水暖房機（給湯・温水暖房一体型）'),
        ('IntegratedElectricHeater', '電気ヒーター式給湯温水暖房機（給湯・温水暖房一体型）'),
        ('Hybrid_Gas', '暖房部：電気ヒートポンプ・ガス、給湯部：ガス（給湯・温水暖房一体型）'),
        ('Hybrid_Hybrid', '暖房部：電気ヒートポンプ・ガス、給湯部：電気ヒートポンプ・ガス（給湯・温水暖房一体型）'),
        ('Gas_Hybrid', '暖房部：ガス、給湯部：電気ヒートポンプ・ガス（給湯・温水暖房一体型）'),
        ('Cogeneration', 'コージェネレーション'),
        ('Other', 'その他の給湯設備機器'),
        ('NotUsed', '給湯熱源機を設置しない'),
    )
    integrated_water_heater_type = models.CharField(
        '給湯熱源種類（給湯・温水暖房一体型）', max_length=31, choices=INTEGRATED_WATER_HEATER_TYPE_LIST, blank=False, default="IntegratedGasLatentHeatRecovery", 
        help_text="給湯熱源機の種類を選択して下さい。「給湯設備機器を設置しない」を選択した場合、「標準設備機器」を想定して一次エネルギー消費量が計算されます。")

    GASOIL_WATER_HEATER_EFFICIENCY_TYPE_LIST = (
        ('Mode', 'モード熱効率'),
        ('Other', '熱効率またはエネルギー消費効率'),
        ('None', '効率を入力しない')
    )
    gasoil_water_heater_efficiency_type = models.CharField(
        '給湯機効率種類（ガス・石油熱源の場合）', max_length=17, choices=GASOIL_WATER_HEATER_EFFICIENCY_TYPE_LIST, default="None", 
        help_text="""給湯機（もしくは給湯温水暖房機の給湯部）の効率の種類を指定します。
        モード熱効率（燃料がガス・石油の場合）とは、JIS S 2075「家庭用ガス・石油温水機器のモード効率測定法」の測定方法による値です。
        エネルギー消費効率（燃料がガスの場合）とは、旧省エネ法において定義される「エネルギー消費効率」（ガス温水機器）に相当します。
        熱効率（燃料が石油の場合）とは、JIS S 3031「石油燃焼機器の試験方法通則」の連続給湯効率試験方法あるいは湯沸効率試験方法による値です。
        """)
    gasoil_water_heater_jis_efficiency_GasClassic_Mode = models.DecimalField(
        'ガス従来型給湯機のモード熱効率[%]', max_digits=3, decimal_places=1, default=70.4, 
        help_text="ガス従来型給湯機（給湯専用型もしくは給湯温水暖房機の給湯部）のモード熱効率[%]を小数点以下1桁まで入力します。")

    gasoil_water_heater_jis_efficiency_GasClassic_Other = models.DecimalField(
        'ガス従来型給湯機のエネルギー消費効率[%]', max_digits=3, decimal_places=1, default=70.4, 
        help_text="ガス従来型給湯機（給湯専用型もしくは給湯温水暖房機の給湯部）のエネルギー消費効率[%]を小数点以下1桁まで入力します。")

    gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Mode = models.DecimalField(
        'ガス潜熱回収型給湯機のモード熱効率[%]）', max_digits=3, decimal_places=1, default=83.6, 
        help_text="ガス潜熱回収型給湯機（給湯専用型もしくは給湯温水暖房機の給湯部）のモード熱効率[%]を小数点以下1桁まで入力します。")

    gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Other = models.DecimalField(
        'ガス潜熱回収型給湯機のエネルギー消費効率[%]', max_digits=3, decimal_places=1, default=83.6, 
        help_text="ガス潜熱回収型給湯機（給湯専用型もしくは給湯温水暖房機の給湯部）のエネルギー消費効率[%]を小数点以下1桁まで入力します。")

    gasoil_water_heater_jis_efficiency_OilClassic_Mode = models.DecimalField(
        '石油従来型給湯機のモード熱効率[%]', max_digits=3, decimal_places=1, default=77.9, 
        help_text="石油従来型給湯機（給湯専用型もしくは給湯温水暖房機の給湯部）のモード熱効率[%]を小数点以下1桁まで入力します。")

    gasoil_water_heater_jis_efficiency_OilClassic_Other = models.DecimalField(
        '石油従来型給湯機の熱効率[%]', max_digits=3, decimal_places=1, default=77.9, 
        help_text="石油従来型給湯機（給湯専用型もしくは給湯温水暖房機の給湯部）の熱効率[%]を小数点以下1桁まで入力します。")

    gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Mode = models.DecimalField(
        '石油潜熱回収型給湯機のモード熱効率[%]', max_digits=3, decimal_places=1, default=81.9, 
        help_text="石油潜熱回収型給湯機（給湯専用型もしくは給湯温水暖房機の給湯部）のモード熱効率[%]を小数点以下1桁まで入力します。")

    gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other = models.DecimalField(
        '石油潜熱回収型給湯機の熱効率[%]', max_digits=3, decimal_places=1, default=81.9, 
        help_text="石油潜熱回収型給湯機（給湯専用型もしくは給湯温水暖房機の給湯部）の熱効率[%]を小数点以下1桁まで入力します。")

    HEATPUMP_WATER_HEATER_EFFICIENCY_TYPE_LIST = (
        ('M1SEJISEfficiency', 'M1スタンダードに基づくJIS相当効率'),
        ('Other', 'JIS効率'),
        ('None', '効率を入力しない')
    )
    heatpump_water_heater_efficiency_type = models.CharField(
        '給湯機効率種類（ヒートポンプ熱源の場合）', max_length=17, choices=HEATPUMP_WATER_HEATER_EFFICIENCY_TYPE_LIST, default="None", 
        help_text="""給湯機の効率の種類を指定します。
        JIS効率とは、JIS C 9220（家庭用ヒートポンプ給湯機）による年間給湯保温効率（JIS）又は年間給湯効率（JIS）です。
        M1スタンダードに基づくJIS相当効率は、2017年10月16日現在、株式会社コロナの機種に限定されます。
        """)
    heatpump_water_heater_jis_efficiency_M1SEJISEfficiency = models.DecimalField(
        'M1スタンダードに基づくJIS相当効率（認定機種限定）', max_digits=2, decimal_places=1, default=3.6, 
        help_text="CO2冷媒電気ヒートポンプ給湯機（給湯専用型）のM1スタンダードに基づくJIS相当効率（認定機種限定）を小数点以下2桁まで入力します。")

    heatpump_water_heater_jis_efficiency_Other = models.DecimalField(
        'ヒートポンプのJIS効率[-]', max_digits=2, decimal_places=1, default=2.7, 
        help_text="CO2冷媒電気ヒートポンプ給湯機（給湯専用型）のJIS効率[-]をは小数点以下1桁まで入力します。")

    gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Mode = models.DecimalField(
        'ガス従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のモード熱効率[%]', max_digits=3, decimal_places=1, default=81.0, 
        help_text="ガス従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のモード熱効率[%]を小数点以下1桁まで入力します。")

    gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Other = models.DecimalField(
        'ガス従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のエネルギー消費効率[%]', max_digits=3, decimal_places=1, default=81.0, 
        help_text="ガス従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のエネルギー消費効率[%]を小数点以下1桁まで入力します。")

    gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Mode = models.DecimalField(
        'ガス潜熱回収型給湯温水暖房機（給湯・温水暖房一体型）暖房部のモード熱効率[%]', max_digits=3, decimal_places=1, default=87.0, 
        help_text="ガス潜熱回収型給湯温水暖房機（給湯・温水暖房一体型）暖房部のモード熱効率[%]を小数点以下1桁まで入力します。")

    gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Other = models.DecimalField(
        'ガス潜熱回収型給湯温水暖房機（給湯・温水暖房一体型）暖房部のエネルギー消費効率[%]', max_digits=3, decimal_places=1, default=87.0, 
        help_text="ガス潜熱回収型給湯温水暖房機（給湯・温水暖房一体型）暖房部のエネルギー消費効率[%]を小数点以下1桁まで入力します。")

    gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Mode = models.DecimalField(
        '石油従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のモード熱効率[%]', max_digits=3, decimal_places=1, default=82.0, 
        help_text="石油従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のモード熱効率[%]を小数点以下1桁まで入力します。")

    gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Other = models.DecimalField(
        '石油従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のエネルギー消費効率[%]', max_digits=3, decimal_places=1, default=82.0, 
        help_text="石油従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のエネルギー消費効率[%]を小数点以下1桁まで入力します。")

    water_heater_name = models.CharField(
        '給湯熱源機の名前', max_length=200, blank=True, default="", 
        help_text="給湯熱源機の名前を入力してください。給湯熱源機が電気ヒートポンプ給湯機で、M1スタンダードに基づくJIS相当効率を入力する場合は必須（認定機種名）です。")

    water_heater_heatpump_unit_input = models.BooleanField(
        'ヒートポンプユニット品番の入力', default=False, 
        help_text="ヒートポンプ・ガス併用型給湯機の品番を入力する場合はチェックして下さい。")
    water_heater_heatpump_unit = models.CharField(
        'ヒートポンプユニット品番', max_length=50, blank=True, 
        help_text="ヒートポンプ・ガス併用型給湯機の場合、または、暖房部：ガス、給湯部：電気ヒートポンプ・ガスの場合のヒートポンプユニットの品番を入力します。")
    WATER_HEATER_HEATPUMP_UNIT_LIST = (
        ('HFC', 'フロン系冷媒'),
        ('Propane', 'プロパン系冷媒'),
    )
    water_heater_heatpump_unit_coolant = models.CharField(
        'ヒートポンプユニット冷媒', max_length=17, choices=WATER_HEATER_HEATPUMP_UNIT_LIST, default="HFC", 
        help_text="ヒートポンプ・ガス併用型給湯機の品番入力がない場合に選択します。（ある場合は無視されます）")
    water_heater_tank_unit = models.CharField(
        '貯湯ユニット品番', max_length=50, blank=True, 
        help_text="ヒートポンプ・ガス併用型給湯機の場合、または、暖房部：ガス、給湯部：電気ヒートポンプ・ガスの場合の貯湯ユニットの品番を入力します。")
    water_heater_backup_boiler = models.CharField(
        '補助熱源機品番', max_length=50, blank=True, 
        help_text="ヒートポンプ・ガス併用型給湯機の場合、または、暖房部：ガス、給湯部：電気ヒートポンプ・ガスの場合の補助熱源機の品番を入力します。")

    WATER_HEATER_TANK_PLACE_LIST = (
        ('Inside', 'タンクユニットを室内に設置する'),
        ('Outside', 'タンクユニットを室外に設置する'),
    )
    water_heater_tank_place = models.CharField(
        'タンクユニット設置場所', max_length=7, choices=WATER_HEATER_TANK_PLACE_LIST, default="Inside", 
        help_text="ヒートポンプ・ガス瞬間式併用型暖房機の場合には、タンクユニットの設置場所を指定します。")

    WATER_HEATER_TANK_CAPACITY_LIST = (
        ('Small', 'タンクユニット（小）'),
        ('Large', 'タンクユニット（大）'),
    )
    water_heater_tank_capacity = models.CharField(
        'タンクユニット容量', max_length=5, choices=WATER_HEATER_TANK_CAPACITY_LIST, default="Large", 
        help_text="ヒートポンプユニットの品番でフロン系冷媒を選択した場合は、タンクユニットの容量を指定します。")

    SOLAR_WATER_HEATER_TYPE_LIST = (
        ('System1', '太陽熱温水器を採用する'),
        ('System2', 'ソーラーシステムを採用する'),
        ('NotInstalled', '設置しない'),
    )
    solar_water_heater_type = models.CharField(
        '太陽熱給湯', max_length=12, choices=SOLAR_WATER_HEATER_TYPE_LIST, default="NotInstalled", 
        help_text="太陽熱利用給湯設備を設置する場合、その種類を選択します。寒冷地では凍結防止に対応した「ソーラーシステム」が必要になります。")

    SOLAR_WATER_HEATER_AREA_TYPE_LIST = (
        ('Total', '集熱部総面積、集熱貯湯部総面積又は集熱器総面積を入力する'),
        ('Effective', '有効集熱面積を入力する'),
    )
    solar_water_heater_area_type = models.CharField(
        '集熱面積の入力方法', max_length=9, choices=SOLAR_WATER_HEATER_AREA_TYPE_LIST, default="System2", 
        help_text="集熱面積の入力方法を選択します。")
    solar_water_heater_area = models.DecimalField(
        '集熱面積[m2]', max_digits=3, decimal_places=1, default=0, 
        help_text="「集熱面積の入力方法」で選択した方法による面積を、小数点以下1桁まで入力します。")

    SOLAR_WATER_HEATER_DIRECTION_LIST = (
        ('EastWest15', '真南から東および西へ15度未満'),
        ('East45', '真南から東へ15度以上45度未満'),
        ('East75', '真南から東へ45度以上75度未満'),
        ('East105', '真南から東へ75度以上105度未満'),
        ('East135', '真南から東へ105度以上135度未満'),
        ('East165', '真南から東へ135度以上165度未満'),
        ('EastWest180', '真南から東および西へ165度以上真北まで'),
        ('West165', '真南から西へ135度以上165度未満'),
        ('West135', '真南から西へ105度以上135度未満'),
        ('West105', '真南から西へ75度以上105度未満'),
        ('West75', '真南から西へ45度以上75度未満'),
        ('West45', '真南から西へ15度以上45度未満'),
    )
    solar_water_heater_direction = models.CharField(
        '集熱パネル方位角', max_length=11, choices=SOLAR_WATER_HEATER_DIRECTION_LIST, default="EastWest15", help_text="パネル設置方位角を選択します。")

    SOLAR_WATER_HEATER_ANGLE_LIST = (
        ('0', '傾斜角0度'),
        ('10', '傾斜角10度'),
        ('20', '傾斜角20度'),
        ('30', '傾斜角30度'),
        ('40', '傾斜角40度'),
        ('50', '傾斜角50度'),
        ('60', '傾斜角60度'),
        ('70', '傾斜角70度'),
        ('80', '傾斜角80度'),
        ('90', '傾斜角90度'),
    )
    solar_water_heater_angle = models.CharField(
        '集熱パネル傾斜角', max_length=2, choices=SOLAR_WATER_HEATER_ANGLE_LIST, default="20", help_text="パネル設置傾斜角を選択します。")
    solar_water_heater_tank_capacity = models.DecimalField(
        '貯湯タンク容量[L]', max_digits=3, decimal_places=0, default=0, 
        help_text="ソーラーシステム(太陽熱給湯2)の場合には貯湯タンクの容量を、整数（1～999）で入力します。")

    BATH_INSULATION_LIST = (
        ('HighInsulation', '高断熱浴槽を採用する'),
        ('Normal', '高断熱浴槽を採用しない'),
    )
    bath_insulation = models.CharField(
        '浴槽の保温措置', max_length=14, choices=BATH_INSULATION_LIST, default="Normal", help_text="高断熱浴槽の採用の有無を選択します。")

    PIPE_TYPE_LIST = (
        ('Branch', '先分岐方式'),
        ('Header', 'ヘッダー方式'),
    )
    pipe_type = models.CharField(
        '配管方式', max_length=6, choices=PIPE_TYPE_LIST, default="Header", help_text="配管方式を選択します。「ヘッダー方式」のほうが省エネになります。")

    PIPE_SAVING_LIST = (
        ('Saving', 'ヘッダー分岐後のすべての配管径が13A以下'),
        ('Normal', 'ヘッダー分岐後のいずれかの配管径が13Aより大きい'),
    )
    pipe_saving = models.CharField(
        'ヘッダー節湯措置', max_length=6, choices=PIPE_SAVING_LIST, default="Saving", help_text="配管方式がヘッダー方式の場合は節湯措置を選択します。")

    KITCHEN_TAP_SAVING_LIST = (
        ('TwoValve', '台所水栓は、旧来の2バルブ水栓とする'),
        ('SavingA', '台所水栓に、手元止水機能を採用する'),
        ('SavingC', '台所水栓に、水優先吐水機能を採用する'),
        ('SavingA, SavingC', '台所水栓に、手元止水機能と水優先吐水機能を採用する'),
    )
    kitchen_tap_saving = models.CharField(
        '台所水栓の節湯機能', max_length=16, choices=KITCHEN_TAP_SAVING_LIST, default="SavingA, SavingC", help_text="台所水栓の節湯機能を選択します。")
    
    BATH_SHOWER_TAP_SAVING_LIST = (
        ('TwoValve', '浴室シャワー水栓は、旧来の2バルブ水栓とする'),
        ('SavingA', '浴室シャワー水栓に、手元止水機能を採用する'),
        ('SavingB', '浴室シャワー水栓に、小流量吐水機能を採用する'),
        ('SavingA, SavingB', '浴室シャワー水栓に、手元止水機能と小流量吐水機能を採用する'),
    )
    bath_shower_tap_saving = models.CharField(
        '浴室シャワーの節湯機能', max_length=16, choices=BATH_SHOWER_TAP_SAVING_LIST, default="SavingA, SavingB", 
        help_text="浴室シャワー水栓の節湯機能を選択します。")
    
    WASH_BOWL_TAP_SAVING_LIST = (
        ('TwoValve', '洗面水栓は、旧来の2バルブ水栓とする'),
        ('SavingC', '洗面水栓に、水優先吐水機能を採用する'),
    )
    wash_bowl_tap_saving = models.CharField(
        '洗面水栓の節湯機能', max_length=8, choices=WASH_BOWL_TAP_SAVING_LIST, default="SavingC", help_text="洗面水栓の節湯機能を選択します。")

    #照明設備
    LIGHTING_LIST = (
        ('LowEfficiency', '白熱灯あり'),
        ('HighEfficiency', '白熱灯なし'),
        ('LED', 'すべてLED照明'),
        ('NotInstalled', '設置しない'),
    )
    ldk_lighting = models.CharField(
        '照明：主居室', max_length=14, choices=LIGHTING_LIST, default="LED", 
        help_text="主居室の、照明設備の種類を選択して下さい。")
    oth_lighting = models.CharField(
        '照明：他居室', max_length=14, choices=LIGHTING_LIST, default="LED", 
        help_text="他居室の、照明設備の種類を選択して下さい。")
    nonldk_lighting = models.CharField(
        '照明：非居室', max_length=14, choices=LIGHTING_LIST, default="LED", 
        help_text="非居室の、照明設備の種類を選択して下さい。")

    MULTI_LIST = (
        ('Multi', '採用'),
        ('Single', '不採用'),
    )
    ldk_multi = models.CharField(
        '多灯分散照明', max_length=6, choices=MULTI_LIST, default="Single", help_text="主居室の多灯分散照明方式の採用を選択します。")

    DIMMING_LIST = (
        ('Dimming', '採用'),
        ('None', '不採用'),
    )
    ldk_dimming = models.CharField(
        '調光：主居室', max_length=7, choices=DIMMING_LIST, default="Dimming", 
        help_text="主居室の、調光可能な照明の採用を選択します。蛍光灯の点灯数を制御できる照明も「調光可能」になります。")
    oth_dimming = models.CharField(
        '調光：他居室', max_length=7, choices=DIMMING_LIST, default="Dimming", 
        help_text="他居室の、調光可能な照明の採用を選択します。蛍光灯の点灯数を制御できる照明も「調光可能」になります。")

    SENSOR_LIST = (
        ('Sensor', '採用'),
        ('None', '不採用'),
    )
    nonldk_sensor = models.CharField(
        '人感センサー', max_length=6, choices=SENSOR_LIST, default="Sensor", 
        help_text="非居室の、人感センサーの採用を選択します。トイレや玄関ポーチに、1か所でも採用されていれば「採用している」になります。")

    #太陽光発電
    PHOTOVOLTAIC_LIST = (
        ('NotInstalled', '設置しない'),
        ('Panel1', '1面'),
        ('Panel2', '2面'),
        ('Panel3', '3面'),
        ('Panel4', '4面'),
    )
    photovoltaic = models.CharField(
        '太陽光発電の設置', max_length=12, choices=PHOTOVOLTAIC_LIST, default="NotInstalled", 
        help_text="太陽光発電を設置する場合、設置する面数を、あるいは「設置しない」を選択して下さい。")

    photovoltaic_power_conditioner_efficiency_input = models.BooleanField('パワコン効率を入力する', default=True, help_text='パワーコンディショナの定格負荷効率を入力する場合はチェックして下さい。')
    photovoltaic_power_conditioner_efficiency = models.DecimalField(
        'パワコン効率[%]', max_digits=4, decimal_places=2, default=92.8, help_text="パワーコンディショナの定格負荷効率を、小数点以下2桁まで入力します。")

    PHOTOVOLTAIC_PANEL_CELL_LIST = (
        ('Silicon', '結晶系'),
        ('Other', '結晶系以外'),
    )
    photovoltaic_panel_1_cell = models.CharField(
        '第1面アレイ種類', max_length=7, choices=PHOTOVOLTAIC_PANEL_CELL_LIST, default="Silicon", help_text="太陽電池アレイ第1面の種類を選択します。")
    photovoltaic_panel_2_cell = models.CharField(
        '第2面アレイ種類', max_length=7, choices=PHOTOVOLTAIC_PANEL_CELL_LIST, default="Silicon", help_text="太陽電池アレイ第2面の種類を選択します。")
    photovoltaic_panel_3_cell = models.CharField(
        '第3面アレイ種類', max_length=7, choices=PHOTOVOLTAIC_PANEL_CELL_LIST, default="Silicon", help_text="太陽電池アレイ第3面の種類を選択します。")
    photovoltaic_panel_4_cell = models.CharField(
        '第4面アレイ種類', max_length=7, choices=PHOTOVOLTAIC_PANEL_CELL_LIST, default="Silicon", help_text="太陽電池アレイ第4面の種類を選択します。")

    photovol_panel_1_capacity = models.DecimalField(
        '第1面容量[kW]', max_digits=4, decimal_places=2, default=2.00, help_text="太陽電池アレイ第1面のシステム容量を小数点以下2桁まで入力します。")
    photovol_panel_2_capacity = models.DecimalField(
        '第2面容量[kW]', max_digits=4, decimal_places=2, default=2.00, help_text="太陽電池アレイ第2面のシステム容量を小数点以下2桁まで入力します。")
    photovol_panel_3_capacity = models.DecimalField(
        '第3面容量[kW]', max_digits=4, decimal_places=2, default=2.00, help_text="太陽電池アレイ第3面のシステム容量を小数点以下2桁まで入力します。")
    photovol_panel_4_capacity = models.DecimalField(
        '第4面容量[kW]', max_digits=4, decimal_places=2, default=2.00, help_text="太陽電池アレイ第4面のシステム容量を小数点以下2桁まで入力します。")

    PHOTOVOL_PANEL_SETUP_LIST = (
        ('Frame', '架台設置形'),
        ('RoofMount', '屋根置き形'),
        ('Other', 'その他'),
    )
    photovol_panel_1_setup = models.CharField(
        '第1面設置方式', max_length=9, choices=PHOTOVOL_PANEL_SETUP_LIST, default="RoofMount", help_text="太陽電池アレイ1の設置方式を選択します。")
    photovol_panel_2_setup = models.CharField(
        '第2面設置方式', max_length=9, choices=PHOTOVOL_PANEL_SETUP_LIST, default="RoofMount", help_text="太陽電池アレイ2の設置方式を選択します。")
    photovol_panel_3_setup = models.CharField(
        '第3面設置方式', max_length=9, choices=PHOTOVOL_PANEL_SETUP_LIST, default="RoofMount", help_text="太陽電池アレイ3の設置方式を選択します。")
    photovol_panel_4_setup = models.CharField(
        '第4面設置方式', max_length=9, choices=PHOTOVOL_PANEL_SETUP_LIST, default="RoofMount", help_text="太陽電池アレイ4の設置方式を選択します。")

    PHOTOVOL_PANEL_DIRECTION_LIST = (
        ('EastWest15', '真南から東および西へ15度未満'),
        ('East45', '真南から東へ15度以上45度未満'),
        ('East75', '真南から東へ45度以上75度未満'),
        ('East105', '真南から東へ75度以上105度未満'),
        ('East135', '真南から東へ105度以上135度未満'),
        ('East165', '真南から東へ135度以上165度未満'),
        ('EastWest180', '真南から東および西へ165度以上真北まで'),
        ('West165', '真南から西へ135度以上165度未満'),
        ('West135', '真南から西へ105度以上135度未満'),
        ('West105', '真南から西へ75度以上105度未満'),
        ('West75', '真南から西へ45度以上75度未満'),
        ('West45', '真南から西へ15度以上45度未満'),
    )
    photovol_panel_1_direction = models.CharField(
        '第1面方位角', max_length=11, choices=PHOTOVOL_PANEL_DIRECTION_LIST, default="EastWest15", help_text="太陽電池パネル1の設置方位角を選択します。")
    photovol_panel_2_direction = models.CharField(
        '第2面方位角', max_length=11, choices=PHOTOVOL_PANEL_DIRECTION_LIST, default="East105", help_text="太陽電池パネル2の設置方位角を選択します。")
    photovol_panel_3_direction = models.CharField(
        '第3面方位角', max_length=11, choices=PHOTOVOL_PANEL_DIRECTION_LIST, default="West105", help_text="太陽電池パネル3の設置方位角を選択します。")
    photovol_panel_4_direction = models.CharField(
        '第4面方位角', max_length=11, choices=PHOTOVOL_PANEL_DIRECTION_LIST, default="EastWest180", help_text="太陽電池パネル4の設置方位角を選択します。")

    PHOTOVOL_PANEL_ANGLE_LIST = (
        ('0', '傾斜角0度'),
        ('10', '傾斜角10度'),
        ('20', '傾斜角20度'),
        ('30', '傾斜角30度'),
        ('40', '傾斜角40度'),
        ('50', '傾斜角50度'),
        ('60', '傾斜角60度'),
        ('70', '傾斜角70度'),
        ('80', '傾斜角80度'),
        ('90', '傾斜角90度'),
    )
    photovol_panel_1_angle = models.CharField(
        '第1面傾斜角', max_length=2, choices=PHOTOVOL_PANEL_ANGLE_LIST, default="20", help_text="太陽電池パネル1の設置傾斜角を選択します。")
    photovol_panel_2_angle = models.CharField(
        '第2面傾斜角', max_length=2, choices=PHOTOVOL_PANEL_ANGLE_LIST, default="20", help_text="太陽電池パネル2の設置傾斜角を選択します。")
    photovol_panel_3_angle = models.CharField(
        '第3面傾斜角', max_length=2, choices=PHOTOVOL_PANEL_ANGLE_LIST, default="20", help_text="太陽電池パネル3の設置傾斜角を選択します。")
    photovol_panel_4_angle = models.CharField(
        '第4面傾斜角', max_length=2, choices=PHOTOVOL_PANEL_ANGLE_LIST, default="20", help_text="太陽電池パネル4の設置傾斜角を選択します。")

    #コージェネレーション
    COGENE_LIST = (
        ('Installed', '設置する'),
        ('NotInstalled', '設置しない'),
    )
    cogene = models.CharField(
        'コージェネレーション設備の設置', max_length=12, choices=COGENE_LIST, default="NotInstalled", 
        help_text="コージェネレーション設備の設置の有無を選択して下さい。")

    COGENE_TYPE_LIST = (
        ('PEFC', 'PEFC(固体高分子形燃料電池)'),
        ('SOFC', 'SOFC(固体酸化物形燃料電池)'),
        ('Before2015', '2015年度以前の評価方法またはGEC'),
    )
    cogene_type = models.CharField(
        'コージェネレーションの種類', max_length=10, choices=COGENE_TYPE_LIST, default="Before2015", 
        help_text="コージェネレーションの種類を選択します。")

    cogene_PEFC_input = models.BooleanField('コージェネレーション機器（PEFC）を指定する', default=False, help_text='コージェネレーション機器（PEFC）を指定する場合はチェックして下さい。')
    cogene_powerunit_PEFC = models.CharField(
        '発電ユニット（PEFC）', max_length=200, blank=True, 
        help_text="コージェネレーション機器（PEFC：固体高分子形燃料電池）の発電ユニットの品番を入力してください。品番の入力がない場合、「PEFC」が初期値として設定されます。")
    cogene_tankunit_PEFC = models.CharField(
        '貯湯ユニット（PEFC）', max_length=200, blank=True, 
        help_text="コージェネレーション機器（PEFC：固体高分子形燃料電池）の貯湯ユニットの品番を入力してください。品番の入力がない場合、「PEFC」が発電ユニットの初期値として設定されます。")
    cogene_backupboiler_PEFC = models.CharField(
        'バックアップボイラー（PEFC）', max_length=200, blank=True, 
        help_text="コージェネレーション機器（PEFC：固体高分子形燃料電池）のバックアップボイラーの品番を入力してください。品番の入力がない場合、「PEFC」が発電ユニットの初期値として設定されます。")
    
    cogene_SOFC_input = models.BooleanField('コージェネレーション機器（SOFC）を指定する', default=False, help_text='コージェネレーション機器（SOFC）を指定する場合はチェックして下さい。')
    cogene_powerunit_SOFC = models.CharField(
        '発電ユニット（SOFC）', max_length=200, blank=True, 
        help_text="コージェネレーション機器（SOFC：固体酸化物形燃料電池）の発電ユニットの品番を入力してください。品番の入力がない場合、「SOFC」が初期値として設定されます。")
    cogene_tankunit_SOFC = models.CharField(
        '貯湯ユニット（SOFC）', max_length=200, blank=True, 
        help_text="コージェネレーション機器（SOFC：固体酸化物形燃料電池）の貯湯ユニットの品番を入力してください。品番の入力がない場合、「SOFC」が発電ユニットの初期値として設定されます。")
    cogene_backupboiler_SOFC = models.CharField(
        'バックアップボイラー（SOFC）', max_length=200, blank=True, 
        help_text="コージェネレーション機器（SOFC：固体酸化物形燃料電池）のバックアップボイラーの品番を入力してください。品番の入力がない場合、「SOFC」が発電ユニットの初期値として設定されます。")

    COGENE_POWERUNIT_LIST = (
        ('PEFC1', 'PEFC1'),
        ('PEFC2', 'PEFC2'),
        ('PEFC3', 'PEFC3'),
        ('PEFC4', 'PEFC4'),
        ('PEFC5', 'PEFC5'),
        ('PEFC6', 'PEFC6'),
        ('SOFC1', 'SOFC1'),
        ('SOFC2', 'SOFC2'),
        ('GEC1', 'GEC1'),
        ('GEC2', 'GEC2'),
    )
    cogene_unit_powerunit_2015 = models.CharField(
        'コージェネ発電ユニット（2015年以前の評価方法またはGEC）', max_length=5, choices=COGENE_POWERUNIT_LIST, default="PEFC1", 
        help_text="コージェネレーションが2015年以前の評価方法またはGECの場合、コージェネレーションの発電ユニットを選択します。")
    
    def nonldk_area_check(self):
        nonldk_area = self.total_area - (self.ldk_area + self.oth_area)
        if nonldk_area >= 0:
            return True
        return False
    
    def __str__(self):
        return str(self.pk)

    def get_pecbyapi_res(self):
        if self.calc_done:
            data = {'Total':[self.resE_T, self.resE_ST, ],
                    'Lighting':[self.resE_L, self.resE_SL, ],
                    'Hotwater':[self.resE_W, self.resE_SW, ],
                    'Ventilation':[self.resE_V, self.resE_SV, ],
                    'Cooling':[self.resE_C, self.resE_SC, ],
                    'Heating':[self.resE_H, self.resE_SH, ],
                    'Other':[self.resE_M, self.resE_SM, ],
                    'ReduceByPV':self.resReduceByPV,
                    'SellByPV':self.resSellByPV,
                    'GenerateByPV':self.resGenerateByPV,
                    'GenerateByCG':self.resGenerateByCG,
                    }
            df = pd.DataFrame(data)
            df['subTotal'] = df['Lighting'] + df['Hotwater'] + df['Ventilation'] + df['Cooling'] + df['Heating']
            df['achievement'] = df['subTotal'][0]/df['subTotal'][1] * 100
            df = df.round().astype(int)
            data = df.to_dict()
            data['ErrMessage'] = ''
        else:
            data = {'ErrMessage':'計算結果がありません'}
        return data

    def get_pecbyapi_fig(self):
        if self.calc_done:
            data = {'Total':[self.resE_T, self.resE_ST, ],
                    'Lighting':[self.resE_L, self.resE_SL, ],
                    'Hotwater':[self.resE_W, self.resE_SW, ],
                    'Ventilation':[self.resE_V, self.resE_SV, ],
                    'Cooling':[self.resE_C, self.resE_SC, ],
                    'Heating':[self.resE_H, self.resE_SH, ],
                    'Other':[self.resE_M, self.resE_SM, ],
                    'ReduceByPV':self.resReduceByPV,
                    'SellByPV':self.resSellByPV,
                    'GenerateByPV':self.resGenerateByPV,
                    'GenerateByCG':self.resGenerateByCG,
                    }
            df = pd.DataFrame(data)
            fig, ax1 = plt.subplots(figsize=(5,2), tight_layout=True)
            p1 = ax1.barh([0,1], df['Lighting'].values, alpha=0.8, color='red')
            p2 = ax1.barh([0,1], df['Hotwater'].values, left=df['Lighting'].values, alpha=0.8, color='green')
            p3 = ax1.barh([0,1], df['Ventilation'].values, left=df['Lighting'].values+df['Hotwater'].values, alpha=0.8, color='purple')
            p4 = ax1.barh([0,1], df['Cooling'].values, left=df['Lighting'].values+df['Hotwater'].values+df['Ventilation'].values, alpha=0.8, color='blue')
            p5 = ax1.barh([0,1], df['Heating'].values, left=df['Lighting'].values+df['Hotwater'].values+df['Ventilation'].values+df['Cooling'].values, alpha=0.8, color='orange')
            ax1.set_yticks([0,1])
            ax1.set_yticklabels(['設計値', '基準値'])
            tmpsum = df['Lighting'][1] + df['Hotwater'][1] + df['Ventilation'][1] + df['Cooling'][1] + df['Heating'][1]
            tmp = int(180) + 21
            ax1.set_xlim(0, tmp)
            ax1.set_xticks(range(0, tmp, 20))
            ax1.grid(True, axis='x')
            ax2 = ax1.twiny()
            #ax2.barh([0,1], df['Total'].values)
            #ax2.broken_barh([(df['Total'][0], 1)], (0, 1), facecolors=('red'))
            ax2.set_xlim(0, tmp)
            ax2.set_xticks([tmpsum*0.25, tmpsum*0.5, tmpsum*0.75, tmpsum])
            ax2.set_xticklabels(['25%', '50%', '75%', '100%'])
            ax2.grid(True, color='red', linestyle='--', linewidth=1)
            buf = BytesIO()
            fig.savefig(buf, format='png', dpi=120)
            image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            graph = image_base64
            buf.close()
            plt.close('all')
        else:
            graph = '計算結果がありません'
        return graph


    def get_ldk_heating_context(self):
        if self.heating_system == 'RoomSpaceHeating':
            if self.ldk_heating_type == 'RoomAirConditioningHeating':
                if self.ldk_ac_heating_efficiency == 'None':
                    ldk_heating_context = ['エネルギー消費効率区分を指定しない',]
                else:
                    ldk_heating_context = [
                        'エアコン効率区分：' + self.get_ldk_ac_heating_efficiency_display(), 
                        '容量可変型コンプレッサー：' + self.get_ldk_ac_heating_compressor_display(), 
                    ]
            elif self.ldk_heating_type == 'FFHeating':
                if self.ldk_ff_saving_input:
                    ldk_heating_context = [
                        'FF暖房効率[%]：' + str(self.ldk_ff_heating_efficiency), 
                    ]
                else:
                    ldk_heating_context = ['エネルギー消費効率を入力しない']
            elif self.ldk_heating_type in ['PanelRadiator', 'FanConvectorRadiator', ]:
                if self.hotwater_heating_system == 'NonIntegrated':
                    if self.hotwater_heating_source_type == 'OilClassic':
                        ldk_heating_context = [
                            '温水暖房熱源システム：' + self.get_hotwater_heating_system_display(), 
                            '温水暖房専用型熱源機器：' + self.get_hotwater_heating_source_type_display(), 
                        ]
                        if self.hotwater_heating_source_saving_input:
                            ldk_heating_context += [
                                'JIS効率[%]：' + str(self.hotwater_heating_source_efficiency_OilClassic), 
                            ]
                        else:
                            ldk_heating_context += [
                                'エネルギー消費効率を入力しない', 
                            ]
                        ldk_heating_context += [
                            '温水暖房配管の断熱：' + self.get_hotwater_heating_source_pipe_display(), 
                        ]
                    elif self.hotwater_heating_source_type == 'GasClassic':
                        ldk_heating_context = [
                            '温水暖房熱源システム：' + self.get_hotwater_heating_system_display(), 
                            '温水暖房専用型熱源機器：' + self.get_hotwater_heating_source_type_display(), 
                        ]
                        if self.hotwater_heating_source_saving_input:
                            ldk_heating_context += [
                                'JIS効率[%]：' + str(self.hotwater_heating_source_efficiency_GasClassic), 
                            ]
                        else:
                            ldk_heating_context += [
                                'エネルギー消費効率を入力しない', 
                            ]
                        ldk_heating_context += [
                            '温水暖房配管の断熱：' + self.get_hotwater_heating_source_pipe_display(), 
                        ]
                    elif self.hotwater_heating_source_type == 'GasLatentHeatRecovery':
                        ldk_heating_context = [
                            '温水暖房熱源システム：' + self.get_hotwater_heating_system_display(), 
                            '温水暖房専用型熱源機器：' + self.get_hotwater_heating_source_type_display(), 
                        ]
                        if self.hotwater_heating_source_saving_input:
                            ldk_heating_context += [
                                'JIS効率[%]：' + str(self.hotwater_heating_source_efficiency_GasLatentHeatRecovery), 
                            ]
                        else:
                            ldk_heating_context += [
                                'エネルギー消費効率を入力しない', 
                            ]
                        ldk_heating_context += [
                            '温水暖房配管の断熱：' + self.get_hotwater_heating_source_pipe_display(), 
                        ]
                    elif self.hotwater_heating_source_type in ['OilLatentHeatRecovery', 'ElectricHeatPump', 'ElectricHeater', ]:
                        ldk_heating_context = [
                            '温水暖房熱源システム：' + self.get_hotwater_heating_system_display(), 
                            '温水暖房専用型熱源機器：' + self.get_hotwater_heating_source_type_display(), 
                            '温水暖房配管の断熱：' + self.get_hotwater_heating_source_pipe_display(), 
                        ]
                elif self.hotwater_heating_system == 'Integrated':
                    ldk_heating_context = [
                        '温水暖房熱源システム：' + self.get_hotwater_heating_system_display(), 
                        '給湯・温水暖房一体型熱源機器：' + self.get_hotwater_heating_source_type_display() + '（※給湯設備参照）', 
                        '温水暖房配管の断熱：' + self.get_hotwater_heating_source_pipe_display(), 
                    ]
                elif self.hotwater_heating_system == 'Cogeneration':
                    ldk_heating_context = [
                        '温水暖房熱源システム：' + self.get_hotwater_heating_system_display(), 
                        '温水暖房熱源機器：' + self.get_hotwater_heating_source_type_display() + '（※コージェネレーション設備の設定を行って下さい。）', 
                        '温水暖房配管の断熱：' + self.get_hotwater_heating_source_pipe_display(), 
                    ]
                elif self.hotwater_heating_system == 'Other':
                    ldk_heating_context = [
                        '温水暖房熱源システム：' + self.get_hotwater_heating_system_display(), 
                        '温水暖房熱源機器：' + self.get_hotwater_heating_source_type_display(), 
                        '熱源機器の名称：', + self.hotwater_heating_source_name, 
                        '温水暖房配管の断熱：' + self.get_hotwater_heating_source_pipe_display(), 
                    ]
                else:
                    ldk_heating_context = ['温水暖房熱源機器：設置しない', ]
            elif self.ldk_heating_type == 'HotWaterFloorHeatingRadiator':
                if self.hotwater_heating_system == 'NonIntegrated':
                    if self.hotwater_heating_source_type == 'OilClassic':
                        ldk_heating_context = [
                            '温水床暖敷設率[%]：' + str(self.ldk_hotwater_floorheating_area_rate), 
                            '上面放熱率[%]：' + str(self.ldk_hotwater_floorheating_upward_heatflow_rate), 
                            '温水暖房熱源システム：' + self.get_hotwater_heating_system_display(), 
                            '温水暖房専用型熱源機器：' + self.get_hotwater_heating_source_type_display(), 
                        ]
                        if self.hotwater_heating_source_saving_input:
                            ldk_heating_context += [
                                'JIS効率[%]：' + str(self.hotwater_heating_source_efficiency_OilClassic), 
                            ]
                        else:
                            ldk_heating_context += [
                                'エネルギー消費効率を入力しない', 
                            ]
                        ldk_heating_context += [
                            '温水暖房配管の断熱：' + self.get_hotwater_heating_source_pipe_display(), 
                        ]
                    elif self.hotwater_heating_source_type == 'GasClassic':
                        ldk_heating_context = [
                            '温水床暖敷設率[%]：' + str(self.ldk_hotwater_floorheating_area_rate), 
                            '上面放熱率[%]：' + str(self.ldk_hotwater_floorheating_upward_heatflow_rate), 
                            '温水暖房熱源システム：' + self.get_hotwater_heating_system_display(), 
                            '温水暖房専用型熱源機器：' + self.get_hotwater_heating_source_type_display(), 
                        ]
                        if self.hotwater_heating_source_saving_input:
                            ldk_heating_context += [
                                'JIS効率[%]：' + str(self.hotwater_heating_source_efficiency_GasClassic), 
                            ]
                        else:
                            ldk_heating_context += [
                                'エネルギー消費効率を入力しない', 
                            ]
                        ldk_heating_context += [
                            '温水暖房配管の断熱：' + self.get_hotwater_heating_source_pipe_display(), 
                        ]
                    elif self.hotwater_heating_source_type == 'GasLatentHeatRecovery':
                        ldk_heating_context = [
                            '温水床暖敷設率[%]：' + str(self.ldk_hotwater_floorheating_area_rate), 
                            '上面放熱率[%]：' + str(self.ldk_hotwater_floorheating_upward_heatflow_rate), 
                            '温水暖房熱源システム：' + self.get_hotwater_heating_system_display(), 
                            '温水暖房専用型熱源機器：' + self.get_hotwater_heating_source_type_display(), 
                        ]
                        if self.hotwater_heating_source_saving_input:
                            ldk_heating_context += [
                                'JIS効率[%]：' + str(self.hotwater_heating_source_efficiency_GasLatentHeatRecovery), 
                            ]
                        else:
                            ldk_heating_context += [
                                'エネルギー消費効率を入力しない', 
                            ]
                        ldk_heating_context += [
                            '温水暖房配管の断熱：' + self.get_hotwater_heating_source_pipe_display(), 
                        ]
                    elif self.hotwater_heating_source_type in ['OilLatentHeatRecovery', 'ElectricHeatPump', 'ElectricHeater', ]:
                        ldk_heating_context = [
                            '温水床暖敷設率[%]：' + str(self.ldk_hotwater_floorheating_area_rate), 
                            '上面放熱率[%]：' + str(self.ldk_hotwater_floorheating_upward_heatflow_rate), 
                            '温水暖房熱源システム：' + self.get_hotwater_heating_system_display(), 
                            '温水暖房専用型熱源機器：' + self.get_hotwater_heating_source_type_display(), 
                            '温水暖房配管の断熱：' + self.get_hotwater_heating_source_pipe_display(), 
                        ]
                    else:
                        ldk_heating_context =['温水暖房専用型熱源機器の選択肢が不正です']
                elif self.hotwater_heating_system == 'Integrated':
                    ldk_heating_context = [
                        '温水床暖敷設率[%]：' + str(self.ldk_hotwater_floorheating_area_rate), 
                        '上面放熱率[%]：' + str(self.ldk_hotwater_floorheating_upward_heatflow_rate), 
                        '温水暖房熱源システム：' + self.get_hotwater_heating_system_display(), 
                        '給湯・温水暖房一体型熱源機器：' + self.get_hotwater_heating_source_type_display() + '（※給湯設備参照）', 
                        '温水暖房配管の断熱：' + self.get_hotwater_heating_source_pipe_display(), 
                    ]
                elif self.hotwater_heating_system == 'Cogeneration':
                    ldk_heating_context = [
                        '温水床暖敷設率[%]：' + str(self.ldk_hotwater_floorheating_area_rate), 
                        '上面放熱率[%]：' + str(self.ldk_hotwater_floorheating_upward_heatflow_rate), 
                        '温水暖房熱源システム：' + self.get_hotwater_heating_system_display(), 
                        '温水暖房熱源機器：' + self.get_hotwater_heating_source_type_display() + '（※コージェネレーション設備の設定を行って下さい。）', 
                        '温水暖房配管の断熱：' + self.get_hotwater_heating_source_pipe_display(), 
                    ]
                elif self.hotwater_heating_system == 'Other':
                    ldk_heating_context = [
                        '温水床暖敷設率[%]：' + str(self.ldk_hotwater_floorheating_area_rate), 
                        '上面放熱率[%]：' + str(self.ldk_hotwater_floorheating_upward_heatflow_rate), 
                        '温水暖房熱源システム：' + self.get_hotwater_heating_system_display(), 
                        '温水暖房熱源機器：' + self.get_hotwater_heating_source_type_display(), 
                        '熱源機器の名称：', + self.hotwater_heating_source_name, 
                        '温水暖房配管の断熱：' + self.get_hotwater_heating_source_pipe_display(), 
                    ]
                else:
                    ldk_heating_context = [
                        '温水床暖敷設率[%]：' + str(self.ldk_hotwater_floorheating_area_rate), 
                        '上面放熱率[%]：' + str(self.ldk_hotwater_floorheating_upward_heatflow_rate), 
                        '温水暖房熱源機器：設置しない', 
                    ]
            elif self.ldk_heating_type == 'ElecricFloorHeating':
                ldk_heating_context = [
                    '温水床暖敷設率[%]：' + str(self.ldk_elecric_floorheating_area_rate), 
                    '上面放熱率[%]：' + str(self.ldk_elecric_floorheating_upward_heatflow_rate), 
                ]
            elif self.ldk_heating_type == 'ElectricRoomHeaterWithThermalStorage':
                ldk_heating_context = []
            elif self.ldk_heating_type == 'FloorHeatingWithRAC':
                ldk_heating_context = [
                    'エアコン床暖敷設率[%]：' + str(self.ldk_ac_floorheating_area_rate), 
                    '上面放熱率[%]：' + str(self.ldk_ac_floorheating_upward_heatflow_rate), 
                    'エアコン床暖配管の断熱：' + self.get_ldk_ac_floorheating_pipe_display(), 
                ]
            elif self.ldk_heating_type == 'OtherHeatingDevice':
                ldk_heating_context = [
                    'その他の暖房機器：' + self.get_ldk_other_heating_device_name_display(), 
                    '機器の名称：', + self.ldk_other_heating_device_name, 
                ]
            else:
                ldk_heating_context = ['暖房設備機器または放熱器を設置しない']

            return ldk_heating_context
        elif self.heating_system == 'AllSpaceHeating':
            if self.heating_rated_input:
                return [
                    '定格暖房能力[W]：' + str(self.heating_rated_capacity), 
                    '定格暖房消費電力[W]：' + str(self.heating_rated_power), 
                    '風量補正の有無：' + self.get_heating_power_correction_display(), 
                    '消費電力補正係数[-]：' + str(self.heating_coefficient), 
                ]
            else:
                return ['定格暖房能力および定格暖房消費電力を入力しない', ]
        else:
            return ['暖房設備を設置しない', ]

    def get_oth_heating_context(self):
        if self.heating_system == 'RoomSpaceHeating':
            if self.oth_heating_type == 'RoomAirConditioningHeating':
                if self.oth_ac_heating_efficiency == 'None':
                    return ['エネルギー消費効率区分を指定しない']
                else:
                    return [
                        'エアコン効率区分：' + self.get_oth_ac_heating_efficiency_display(), 
                        '容量可変型コンプレッサー：' + self.get_oth_ac_heating_compressor_display(), 
                        ]
            elif self.oth_heating_type == 'FFHeating':
                if self.oth_ff_saving_input:
                    return [
                        'FF暖房効率[%]：' + str(self.oth_ff_heating_efficiency), 
                        ]
                else:
                    return ['エネルギー消費効率を入力しない']
            elif self.oth_heating_type in ['PanelRadiator', 'FanConvectorRadiator', ]:
                if self.ldk_heating_type in ['PanelRadiator', 'FanConvectorRadiator', 'HotWaterFloorHeatingRadiator']:
                    hotwater_heating_source_type_txt = '※主居室参照'
                    hotwater_heating_source_efficiency_txt = '※主居室参照'
                    hotwater_heating_source_pipe_txt = '※主居室参照'
                    hotwater_heating_source_name_txt = '※主居室参照'
                else:
                    hotwater_heating_source_type_txt = self.get_hotwater_heating_source_type_display()
                    hotwater_heating_source_efficiency_txt = str(self.hotwater_heating_source_efficiency)
                    hotwater_heating_source_pipe_txt = self.get_hotwater_heating_source_pipe_display()
                    hotwater_heating_source_name_txt = self.hotwater_heating_source_name

                if self.hotwater_heating_source_type in ['OilClassic', 'GasClassic', 'GasLatentHeatRecovery', ]:
                    if self.hotwater_heating_source_saving_input:
                        return [
                            '温水暖房熱源機：' + hotwater_heating_source_type_txt, 
                            'JIS効率[%]：' + hotwater_heating_source_efficiency_txt, 
                            '温水暖房配管の断熱：' + hotwater_heating_source_pipe_txt, 
                            ]
                    else:
                        return [
                            'エネルギー消費効率を入力しない', 
                            '温水暖房配管の断熱：' + hotwater_heating_source_pipe_txt, 
                            ]
                elif self.hotwater_heating_source_type in ['OilLatentHeatRecovery', 'ElectricHeatPump', 'ElectricHeater', ]:
                    return [
                        '温水暖房熱源機：' + hotwater_heating_source_type_txt, 
                        '温水暖房配管の断熱：' + hotwater_heating_source_pipe_txt, 
                        ]
                elif self.hotwater_heating_source_type == 'Cogeneration':
                    return [
                        '温水暖房熱源機：' + hotwater_heating_source_type_txt, 
                        '温水暖房配管の断熱：' + hotwater_heating_source_pipe_txt, 
                        ]
                elif self.hotwater_heating_source_type == 'Integrated':
                    return [
                        '温水暖房熱源機：' + hotwater_heating_source_type_txt, 
                        '温水暖房配管の断熱：' + hotwater_heating_source_pipe_txt, 
                        ]
                elif self.hotwater_heating_source_type == 'Other':
                    return [
                        '温水暖房熱源機：' + hotwater_heating_source_type_txt, 
                        '機器の名称：', + hotwater_heating_source_name_txt, 
                        '温水暖房配管の断熱：' + hotwater_heating_source_pipe_txt, 
                        ]
                else:
                    return ['温水暖房熱源機：設置しない']
            elif self.oth_heating_type == 'HotWaterFloorHeatingRadiator':
                if self.ldk_heating_type in ['PanelRadiator', 'FanConvectorRadiator', 'HotWaterFloorHeatingRadiator']:
                    hotwater_heating_source_type_txt = '※主居室参照'
                    hotwater_heating_source_efficiency_txt = '※主居室参照'
                    hotwater_heating_source_pipe_txt = '※主居室参照'
                    hotwater_heating_source_name_txt = '※主居室参照'
                else:
                    hotwater_heating_source_type_txt = self.get_hotwater_heating_source_type_display()
                    hotwater_heating_source_efficiency_txt = str(self.hotwater_heating_source_efficiency)
                    hotwater_heating_source_pipe_txt = self.get_hotwater_heating_source_pipe_display()
                    hotwater_heating_source_name_txt = self.hotwater_heating_source_name

                if self.hotwater_heating_source_type in ['OilClassic', 'GasClassic', 'GasLatentHeatRecovery', ]:
                    if self.hotwater_heating_source_saving_input:
                        return [
                            '温水床暖敷設率[%]：' + str(self.oth_hotwater_floorheating_area_rate), 
                            '上面放熱率[%]：' + str(self.oth_hotwater_floorheating_upward_heatflow_rate), 
                            '温水暖房熱源機：' + hotwater_heating_source_type_txt, 
                            'JIS効率[%]：' + hotwater_heating_source_efficiency_txt, 
                            '温水暖房配管の断熱：' + hotwater_heating_source_pipe_txt, 
                            ]
                    else:
                        return [
                            '温水床暖敷設率[%]：' + str(self.oth_hotwater_floorheating_area_rate), 
                            '上面放熱率[%]：' + str(self.oth_hotwater_floorheating_upward_heatflow_rate), 
                            'エネルギー消費効率を入力しない', 
                            '温水暖房配管の断熱：' + hotwater_heating_source_pipe_txt, 
                            ]
                elif self.hotwater_heating_source_type in ['OilLatentHeatRecovery', 'ElectricHeatPump', 'ElectricHeater', ]:
                    return [
                        '温水床暖敷設率[%]：' + str(self.oth_hotwater_floorheating_area_rate), 
                        '上面放熱率[%]：' + str(self.oth_hotwater_floorheating_upward_heatflow_rate), 
                        '温水暖房熱源機：' + hotwater_heating_source_type_txt, 
                        '温水暖房配管の断熱：' + hotwater_heating_source_pipe_txt, 
                        ]
                elif self.hotwater_heating_source_type == 'Cogeneration':
                    return [
                        '温水床暖敷設率[%]：' + str(self.oth_hotwater_floorheating_area_rate), 
                        '上面放熱率[%]：' + str(self.oth_hotwater_floorheating_upward_heatflow_rate), 
                        '温水暖房熱源機：' + hotwater_heating_source_type_txt, 
                        '温水暖房配管の断熱：' + hotwater_heating_source_pipe_txt, 
                        ]
                elif self.hotwater_heating_source_type == 'Integrated':
                    return [
                        '温水床暖敷設率[%]：' + str(self.oth_hotwater_floorheating_area_rate), 
                        '上面放熱率[%]：' + str(self.oth_hotwater_floorheating_upward_heatflow_rate), 
                        '温水暖房熱源機：' + hotwater_heating_source_type_txt, 
                        '温水暖房配管の断熱：' + hotwater_heating_source_pipe_txt, 
                        ]
                elif self.hotwater_heating_source_type == 'Other':
                    return [
                        '温水床暖敷設率[%]：' + str(self.oth_hotwater_floorheating_area_rate), 
                        '上面放熱率[%]：' + str(self.oth_hotwater_floorheating_upward_heatflow_rate), 
                        '温水暖房熱源機：' + hotwater_heating_source_type_txt, 
                        '機器の名称：', + hotwater_heating_source_name_txt, 
                        '温水暖房配管の断熱：' + hotwater_heating_source_pipe_txt, 
                        ]
                else:
                    return [
                        '温水床暖敷設率[%]：' + str(self.oth_hotwater_floorheating_area_rate), 
                        '上面放熱率[%]：' + str(self.oth_hotwater_floorheating_upward_heatflow_rate), 
                        '温水暖房熱源機：設置しない', 
                        ]
            elif self.oth_heating_type == 'ElecricFloorHeating':
                return [
                    '温水床暖敷設率[%]：' + str(self.oth_elecric_floorheating_area_rate), 
                    '上面放熱率[%]：' + str(self.oth_elecric_floorheating_upward_heatflow_rate), 
                    ]
            elif self.oth_heating_type == 'ElectricRoomHeaterWithThermalStorage':
                pass
            elif self.oth_heating_type == 'FloorHeatingWithRAC':
                return [
                    'エアコン床暖敷設率[%]：' + str(self.oth_ac_floorheating_area_rate), 
                    '上面放熱率[%]：' + str(self.oth_ac_floorheating_upward_heatflow_rate), 
                    'エアコン床暖配管の断熱：' + self.get_oth_ac_floorheating_pipe_display(), 
                    ]
            elif self.oth_heating_type == 'ElectricHeatPumpCentralHeating':
                pass
            elif self.oth_heating_type == 'OtherHeatingDevice':
                return [
                    'その他の暖房機器：' + self.get_oth_other_heating_device_name_display(), 
                    '機器の名称：', + self.oth_other_heating_device_name, 
                    ]
            else:
                return ['暖房設備機器または放熱器を設置しない']
        elif self.heating_system == 'AllSpaceHeating':
                return ['住戸全体を暖房する']
        else:
            return ['暖房設備を設置しない']

    def get_ldk_cooling_context(self):
        if self.cooling_system == 'RoomSpaceCooling':
            if self.ldk_cooling_type == 'RoomAirConditioningCooling':
                if self.ldk_heating_type == 'RoomAirConditioningHeating':
                    return ['※暖房設備参照']
                else:
                    if self.ldk_ac_cooling_efficiency == 'None':
                        return ['エネルギー消費効率区分を指定しない']
                    else:
                        return [
                            'エアコン効率区分：' + self.get_ldk_ac_cooling_efficiency_display(), 
                            '容量可変型コンプレッサー：' + self.get_ldk_ac_cooling_compressor_display(), 
                            ]
            elif self.ldk_cooling_type == 'OtherCoolingDevice':
                return [
                    'その他の冷房設備機器：' + self.ldk_other_cooling_device_name, 
                    ]
            else:
                return ['冷房設備機器を設置しない']
        elif self.cooling_system == 'AllSpaceCooling':
            return ['※暖房設備参照']
        else:
            return ['冷房設備を設置しない']

    def get_oth_cooling_context(self):
        if self.cooling_system == 'RoomSpaceCooling':
            if self.oth_cooling_type == 'RoomAirConditioningCooling':
                if self.oth_heating_type == 'RoomAirConditioningHeating':
                    return ['※暖房設備参照']
                else:
                    if self.oth_ac_cooling_efficiency == 'None':
                        return ['エネルギー消費効率区分を指定しない']
                    else:
                        return [
                            'エアコン効率区分：' + self.get_oth_ac_cooling_efficiency_display(), 
                            '容量可変型コンプレッサー：' + self.get_oth_ac_cooling_compressor_display(), 
                            ]
            elif self.oth_cooling_type == 'OtherCoolingDevice':
                return [
                    'その他の冷房設備機器：' + self.oth_other_cooling_device_name, 
                    ]
            else:
                return ['冷房設備機器を設置しない']
        elif self.cooling_system == 'AllSpaceCooling':
            return ['住戸全体を冷房する']
        else:
            return ['冷房設備を設置しない']

    def get_ventilation_context(self):
        if self.ventilation_type == 'DuctVenitlation1':
            if self.ventilation_heatexchanger == 'HeatExchanger':
                if self.ventilation_saving in ['ThickDuctOnly', 'ThickDuctAndDCMotor', ]:
                    return [
                        '換気設備の省エネ手法：' + self.get_ventilation_saving_display(), 
                        '換気回数[回/h]：' + self.get_ventilation_frequency_display(), 
                        '有効換気量率[-]：' + str(self.ventilation_efficiency), 
                        '温度交換効率[%]：' + str(self.ventilation_heatexchanger_efficiency), 
                        '給気と排気の比率による温度交換効率の補正係数[-]：' + str(self.ventilation_heatexchanger_bal), 
                        '排気過多時における住宅外皮経由の漏気による温度交換効率の補正係数[-]：' + str(self.ventilation_heatexchanger_leak), 
                        ]
                elif self.ventilation_saving == 'SFP':
                    return [
                        '比消費電力：' + str(self.ventilation_sfp), 
                        '換気回数[回/h]：' + self.get_ventilation_frequency_display(), 
                        '有効換気量率[-]：' + str(self.ventilation_efficiency), 
                        '温度交換効率[%]：' + str(self.ventilation_heatexchanger_efficiency), 
                        '給気と排気の比率による温度交換効率の補正係数[-]：' + str(self.ventilation_heatexchanger_bal), 
                        '排気過多時における住宅外皮経由の漏気による温度交換効率の補正係数[-]：' + str(self.ventilation_heatexchanger_leak), 
                        ]
                else:
                    return [
                        '省エネルギー対策を指定しない', 
                        '換気回数[回/h]：' + self.get_ventilation_frequency_display(), 
                        '有効換気量率[-]：' + str(self.ventilation_efficiency), 
                        '温度交換効率[%]：' + str(self.ventilation_heatexchanger_efficiency), 
                        '給気と排気の比率による温度交換効率の補正係数[-]：' + str(self.ventilation_heatexchanger_bal), 
                        '排気過多時における住宅外皮経由の漏気による温度交換効率の補正係数[-]：' + str(self.ventilation_heatexchanger_leak), 
                        ]
            else:
                if self.ventilation_saving in ['ThickDuctOnly', 'ThickDuctAndDCMotor', ]:
                    return [
                        '換気設備の省エネ手法：' + self.get_ventilation_saving_display(), 
                        '換気回数[回/h]：' + self.get_ventilation_frequency_display(), 
                        '有効換気量率[-]：' + str(self.ventilation_efficiency), 
                        ]
                elif self.ventilation_saving == 'SFP':
                    return [
                        '比消費電力：' + str(self.ventilation_sfp), 
                        '換気回数[回/h]：' + self.get_ventilation_frequency_display(), 
                        '有効換気量率[-]：' + str(self.ventilation_efficiency), 
                        ]
                else:
                    return [
                        '省エネルギー対策を指定しない', 
                        '換気回数[回/h]：' + self.get_ventilation_frequency_display(), 
                        '有効換気量率[-]：' + str(self.ventilation_efficiency), 
                        ]
        elif self.ventilation_type == 'DuctVentilation2or3':
            if self.ventilation_saving in ['ThickDuctOnly', 'ThickDuctAndDCMotor', ]:
                return [
                    '換気設備の省エネ手法：' + self.get_ventilation_saving_display(), 
                    '換気回数[回/h]：' + self.get_ventilation_frequency_display(), 
                    ]
            elif self.ventilation_saving == 'SFP':
                return [
                    '比消費電力：' + str(self.ventilation_sfp), 
                    '換気回数[回/h]：' + self.get_ventilation_frequency_display(), 
                    ]
            else:
                return [
                    '省エネルギー対策を指定しない', 
                    '換気回数[回/h]：' + self.get_ventilation_frequency_display(), 
                    ]
        elif self.ventilation_type == 'WallMount1':
            if self.ventilation_heatexchanger == 'HeatExchanger':
                if self.ventilation_saving in ['ThickDuctOnly', 'ThickDuctAndDCMotor', ]:
                    return [
                        '壁付け式第1種換気設備では、この省エネルギー対策を指定できません。', 
                        ]
                elif self.ventilation_saving == 'SFP':
                    return [
                        '比消費電力：' + str(self.ventilation_sfp), 
                        '換気回数[回/h]：' + self.get_ventilation_frequency_display(), 
                        '有効換気量率[-]：' + str(self.ventilation_efficiency), 
                        '温度交換効率[%]：' + str(self.ventilation_heatexchanger_efficiency), 
                        '給気と排気の比率による温度交換効率の補正係数[-]：' + str(self.ventilation_heatexchanger_bal), 
                        '排気過多時における住宅外皮経由の漏気による温度交換効率の補正係数[-]：' + str(self.ventilation_heatexchanger_leak), 
                        ]
                else:
                    return [
                        '省エネルギー対策を指定しない', 
                        '換気回数[回/h]：' + self.get_ventilation_frequency_display(), 
                        '有効換気量率[-]：' + str(self.ventilation_efficiency), 
                        '温度交換効率[%]：' + str(self.ventilation_heatexchanger_efficiency), 
                        '給気と排気の比率による温度交換効率の補正係数[-]：' + str(self.ventilation_heatexchanger_bal), 
                        '排気過多時における住宅外皮経由の漏気による温度交換効率の補正係数[-]：' + str(self.ventilation_heatexchanger_leak), 
                        ]
            else:
                if self.ventilation_saving in ['ThickDuctOnly', 'ThickDuctAndDCMotor', ]:
                    return [
                        '壁付け式第1種換気設備では、この省エネルギー対策を指定できません。', 
                        ]
                elif self.ventilation_saving == 'SFP':
                    return [
                        '比消費電力：' + str(self.ventilation_sfp), 
                        '換気回数[回/h]：' + self.get_ventilation_frequency_display(), 
                        '有効換気量率[-]：' + str(self.ventilation_efficiency), 
                        ]
                else:
                    return [
                        '省エネルギー対策を指定しない', 
                        '換気回数[回/h]：' + self.get_ventilation_frequency_display(), 
                        '有効換気量率[-]：' + str(self.ventilation_efficiency), 
                        ]
        elif self.ventilation_type == 'WallMount2or3':
            if self.ventilation_saving in ['ThickDuctOnly', 'ThickDuctAndDCMotor', ]:
                return [
                    '壁付け式第2種換気設備または壁付け式第3種換気設備では、この省エネルギー対策を指定できません。', 
                    ]
            elif self.ventilation_saving == 'SFP':
                return [
                    '比消費電力：' + str(self.ventilation_sfp), 
                    '換気回数[回/h]：' + self.get_ventilation_frequency_display(), 
                    ]
            else:
                return [
                    '省エネルギー対策を指定しない', 
                    '換気回数[回/h]：' + self.get_ventilation_frequency_display(), 
                    ]
        else:
            return ['換気設備の設定が不正です。']

    def get_hotwater_context(self):
        if self.bathroom in ['TapAndBath', 'TapOnly']:
            if self.hotwater_heating_system == 'Integrated':
                if self.integrated_water_heater_type == 'IntegratedGasClassic':
                    if self.gasoil_water_heater_efficiency_type == 'Mode':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                            '・暖房部熱効率[%]：' + str(self.gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Mode), 
                            '・給湯部モード熱効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_GasClassic_Mode), 
                            ]
                    elif self.gasoil_water_heater_efficiency_type == 'Other':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                            '・暖房部熱効率[%]：' + str(self.gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Other), 
                            '・給湯部エネルギー消費効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_GasClassic_Other), 
                            ]
                    else:
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                            '・効率を入力しない', 
                            ]
                elif self.integrated_water_heater_type =='IntegratedGasLatentHeatRecovery':
                    if self.gasoil_water_heater_efficiency_type == 'Mode':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                            '・暖房部熱効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Mode), 
                            '・給湯部モード熱効率[%]：' + str(self.gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Mode), 
                            ]
                    elif self.gasoil_water_heater_efficiency_type == 'Other':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                            '・暖房部熱効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other), 
                            '・給湯部エネルギー消費効率[%]：' + str(self.gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Other), 
                            ]
                    else:
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                            '・効率を入力しない', 
                            ]
                elif self.integrated_water_heater_type == 'IntegratedOil':
                    if self.gasoil_water_heater_efficiency_type == 'Mode':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                            '・暖房部熱効率[%]：' + str(self.gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Mode), 
                            '・給湯部モード熱効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_OilClassic_Mode), 
                            ]
                    elif self.gasoil_water_heater_efficiency_type == 'Other':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                            '・暖房部熱効率[%]：' + str(self.gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Other), 
                            '・給湯部熱効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_OilClassic_Other), 
                            ]
                    else:
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                            '・効率を入力しない', 
                            ]
                elif self.integrated_water_heater_type == 'IntegratedOilLatentHeatRecovery':
                    if self.gasoil_water_heater_efficiency_type == 'Mode':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                            '・給湯部モード熱効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Mode), 
                            ]
                    elif self.gasoil_water_heater_efficiency_type == 'Other':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                            '・給湯部熱効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other), 
                            ]
                    else:
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                            '・効率を入力しない', 
                            ]
                elif self.integrated_water_heater_type == 'IntegratedElectricHeater':
                    hotwater_context = [
                        '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                        ]
                elif self.integrated_water_heater_type == 'Hybrid_Gas':
                    hotwater_context = [
                        '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                        '・タンクユニット設置場所：' + self.get_water_heater_tank_place_display(), 
                        ]
                elif self.integrated_water_heater_type == 'Hybrid_Hybrid':
                    hotwater_context = [
                        '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                        ]
                elif self.integrated_water_heater_type == 'Gas_Hybrid':
                    if self.water_heater_heatpump_unit_input:
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                            '・ヒートポンプユニット品番：' + self.water_heater_heatpump_unit, 
                            '・貯湯ユニット品番：' + self.water_heater_tank_unit, 
                            '・補助熱源機品番：' + self.water_heater_backup_boiler, 
                            '・タンクユニット設置場所：' + self.get_water_heater_tank_place_display(), 
                            ]
                    else:
                        if self.water_heater_heatpump_unit_coolant == 'HFC':
                            hotwater_context = [
                                '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                                '・ヒートポンプユニット冷媒：' + self.get_water_heater_heatpump_unit_coolant_display(), 
                                '・タンクユニット容量：' + self.get_water_heater_tank_capacity_display(), 
                                ]
                        else:
                            hotwater_context = [
                                '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                                '・ヒートポンプユニット冷媒：' + self.get_water_heater_heatpump_unit_coolant_display(), 
                                ]
                elif self.integrated_water_heater_type == 'Cogeneration':
                    hotwater_context = [
                        '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                        ]
                elif self.integrated_water_heater_type == 'Other':
                    hotwater_context = [
                        '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                        '・給湯熱源機の名前：' + self.water_heater_name, 
                        ]
                else:
                    hotwater_context = [
                        '給湯熱源種類：' + self.get_integrated_water_heater_type_display(),
                        ]
            else:
                if self.water_heater_type == 'GasClassic':
                    if self.gasoil_water_heater_efficiency_type == 'Mode':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・モード熱効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_GasClassic_Mode), 
                            ]
                    elif self.gasoil_water_heater_efficiency_type == 'Other':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・エネルギー消費効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_GasClassic_Other), 
                            ]
                    else:
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・効率を入力しない', 
                            ]
                elif self.water_heater_type == 'GasLatentHeatRecovery':
                    if self.gasoil_water_heater_efficiency_type == 'Mode':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・モード熱効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Mode), 
                            ]
                    elif self.gasoil_water_heater_efficiency_type == 'Other':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・エネルギー消費効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Other), 
                            ]
                    else:
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・効率を入力しない', 
                            ]
                elif self.water_heater_type == 'OilClassic':
                    if self.gasoil_water_heater_efficiency_type == 'Mode':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・モード熱効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_OilClassic_Mode), 
                            ]
                    elif self.water_heater_efficiency_type == 'Other':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・熱効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_OilClassic_Other), 
                            ]
                    else:
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・効率を入力しない', 
                            ]
                elif self.water_heater_type == 'OilLatentHeatRecovery':
                    if self.gasoil_water_heater_efficiency_type == 'Mode':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・モード熱効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Mode), 
                            ]
                    elif self.water_heater_efficiency_type == 'Other':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・熱効率[%]：' + str(self.gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other), 
                            ]
                    else:
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・効率を入力しない', 
                            ]
                elif self.water_heater_type == 'ElectricHeater':
                    hotwater_context = [
                        '給湯熱源種類：' + self.get_water_heater_type_display(),
                        ]
                elif self.water_heater_type == 'ElectricHeatPump':
                    if self.heatpump_water_heater_efficiency_type == 'M1SEJISEfficiency':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・給湯熱源機の名前：' + self.water_heater_name, 
                            '・M1スタンダードJIS相当効率（認定機種限定）[-]：' + str(self.heatpump_water_heater_jis_efficiency_M1SEJISEfficiency), 
                            ]
                    elif self.heatpump_water_heater_efficiency_type == 'Other':
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・JIS効率[-]：' + str(self.heatpump_water_heater_jis_efficiency_Other), 
                            ]
                    else:
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・効率を入力しない', 
                            ]
                elif self.water_heater_type == 'Hybrid':
                    if self.water_heater_heatpump_unit_input:
                        hotwater_context = [
                            '給湯熱源種類：' + self.get_water_heater_type_display(),
                            '・ヒートポンプユニット品番：' + self.water_heater_heatpump_unit, 
                            '・貯湯ユニット品番：' + self.water_heater_tank_unit, 
                            '・補助熱源機品番：' + self.water_heater_backup_boiler, 
                            '・タンクユニット設置場所：' + self.get_water_heater_tank_place_display(), 
                            ]
                    else:
                        if self.water_heater_heatpump_unit_coolant == 'HFC':
                            hotwater_context = [
                                '給湯熱源種類：' + self.get_water_heater_type_display(),
                                '・ヒートポンプユニット冷媒：' + self.get_water_heater_heatpump_unit_coolant_display(), 
                                '・タンクユニット容量：' + self.get_water_heater_tank_capacity_display(), 
                                ]
                        else:
                            hotwater_context = [
                                '給湯熱源種類：' + self.get_water_heater_type_display(),
                                '・ヒートポンプユニット冷媒：' + self.get_water_heater_heatpump_unit_coolant_display(), 
                                ]
                elif self.water_heater_type == 'Cogeneration':
                    hotwater_context = [
                        '給湯熱源種類：' + self.get_water_heater_type_display(),
                        ]
                elif self.water_heater_type == 'Other':
                    hotwater_context = [
                        '給湯熱源種類：' + self.get_water_heater_type_display(),
                        '・給湯熱源機の名前：' + self.water_heater_name, 
                        ]
                else:
                    hotwater_context = [
                        '給湯熱源種類：' + self.get_water_heater_type_display(),
                        ]

            if self.pipe_type == 'Header':
                hotwater_context += [
                    '配管方式：' + self.get_pipe_type_display() + '（' + self.get_pipe_saving_display() + '）', 
                    ]
            else:
                hotwater_context += [
                    '配管方式：' + self.get_pipe_type_display(), 
                    ]
            hotwater_context += [
                '台所水栓の節湯機能：' + self.get_kitchen_tap_saving_display(), 
                '浴室シャワーの節湯機能：' + self.get_bath_shower_tap_saving_display(), 
                '洗面水栓の節湯機能：' + self.get_wash_bowl_tap_saving_display(), 
                '浴槽の保温措置：' + self.get_bath_insulation_display(), 
                ]

            if self.solar_water_heater_type == 'System1':
                hotwater_context += [
                    '太陽熱給湯：' + self.get_solar_water_heater_type_display(), 
                    '集熱面積の入力方法：' + self.get_solar_water_heater_area_type_display(), 
                    '集熱面積[m2]：' + str(self.solar_water_heater_area), 
                    '集熱パネル方位角：' + self.get_solar_water_heater_direction_display(), 
                    '集熱パネル傾斜角：' + self.get_solar_water_heater_angle_display(), 
                    ]
            elif self.solar_water_heater_type == 'System2':
                hotwater_context += [
                    '太陽熱給湯：' + self.get_solar_water_heater_type_display(), 
                    '集熱面積の入力方法：' + self.get_solar_water_heater_area_type_display(), 
                    '集熱面積[m2]：' + str(self.solar_water_heater_area), 
                    '集熱パネル方位角：' + self.get_solar_water_heater_direction_display(), 
                    '集熱パネル傾斜角：' + self.get_solar_water_heater_angle_display(), 
                    '貯湯タンク容量[L]：' + str(self.solar_water_heater_tank_capacity), 
                    ]
            else:
                hotwater_context += [
                    '太陽熱給湯：' + self.get_solar_water_heater_type_display(), 
                    ]

            return hotwater_context
        else:
            return ['給湯設備無し', ]

    def get_ldk_lighting_context(self):
        if self.ldk_lighting in ['LED', 'HighEfficiency', ]:
            ldk_lighting_context = [
                #'主居室の照明：' + self.get_ldk_lighting_display(),
                '多灯分散照明：' + self.get_ldk_multi_display(),
                '調光照明：' + self.get_ldk_dimming_display(),
                ]
        elif self.ldk_lighting == 'LowEfficiency':
            ldk_lighting_context = [
                '調光照明：' + self.get_ldk_dimming_display(),
                ]
        else:
            ldk_lighting_context = [
                #'主居室の照明：' + self.get_ldk_lighting_display(),
                ]
        return ldk_lighting_context

    def get_oth_lighting_context(self):
        if self.oth_lighting in ['LED', 'HighEfficiency', 'LowEfficiency', ]:
            oth_lighting_context = [
                '調光照明：' + self.get_oth_dimming_display(),
                ]
        else:
            oth_lighting_context = [
                ]
        return oth_lighting_context

    def get_nonldk_lighting_context(self):
        if self.nonldk_lighting in ['LED', 'HighEfficiency', 'LowEfficiency', ]:
            nonldk_lighting_context = [
                '人感センサー：' + self.get_nonldk_sensor_display(),
                ]
        else:
            nonldk_lighting_context = [
                ]
        return nonldk_lighting_context

    def get_photovoltaic_base_context(self):
        if self.photovoltaic in ['Panel1', 'Panel2', 'Panel3', 'Panel4', ]:
            photovoltaic_base_context = [
                '設置面数：' + self.get_photovoltaic_display(),
                ]
            if self.photovoltaic_power_conditioner_efficiency_input:
                photovoltaic_base_context += [
                    'パワコン効率[%]：' + str(self.photovoltaic_power_conditioner_efficiency),
                    ]
        else:
            photovoltaic_base_context = [
                '太陽光発電を' + self.get_photovoltaic_display(),
                ]
        return photovoltaic_base_context

    def get_photovoltaic_1_context(self):
        photovoltaic_1_context = [
            '・容量[kW]：' + str(self.photovol_panel_1_capacity),
            '・アレイ種類：' + self.get_photovoltaic_panel_1_cell_display(),
            '・設置方式：' + self.get_photovol_panel_1_setup_display(),
            '・方位角：' + self.get_photovol_panel_1_direction_display(),
            '・傾斜角：' + self.get_photovol_panel_1_angle_display(),
            ]
        return photovoltaic_1_context

    def get_photovoltaic_2_context(self):
        photovoltaic_2_context = [
            '・容量[kW]：' + str(self.photovol_panel_2_capacity),
            '・アレイ種類：' + self.get_photovoltaic_panel_2_cell_display(),
            '・設置方式：' + self.get_photovol_panel_2_setup_display(),
            '・方位角：' + self.get_photovol_panel_2_direction_display(),
            '・傾斜角：' + self.get_photovol_panel_2_angle_display(),
            ]
        return photovoltaic_2_context

    def get_photovoltaic_3_context(self):
        photovoltaic_3_context = [
            '・容量[kW]：' + str(self.photovol_panel_3_capacity),
            '・アレイ種類：' + self.get_photovoltaic_panel_3_cell_display(),
            '・設置方式：' + self.get_photovol_panel_3_setup_display(),
            '・方位角：' + self.get_photovol_panel_3_direction_display(),
            '・傾斜角：' + self.get_photovol_panel_3_angle_display(),
            ]
        return photovoltaic_3_context

    def get_photovoltaic_4_context(self):
        photovoltaic_4_context = [
            '・容量[kW]：' + str(self.photovol_panel_4_capacity),
            '・アレイ種類：' + self.get_photovoltaic_panel_4_cell_display(),
            '・設置方式：' + self.get_photovol_panel_4_setup_display(),
            '・方位角：' + self.get_photovol_panel_4_direction_display(),
            '・傾斜角：' + self.get_photovol_panel_4_angle_display(),
            ]
        return photovoltaic_4_context

    def get_cogene_context(self):
        if self.cogene == 'Installed':
            cogene_context = [
                'コージェネレーションの種類：' + self.get_cogene_type_display(),
                ]
            if self.cogene_type == 'PEFC':
                if self.cogene_PEFC_input:
                    self.cogene_powerunit_PEFC = 'PEFC'
                    self.cogene_tankunit_PEFC = 'PEFC'
                    self.cogene_backupboiler_PEFC = 'PEFC'
                else:
                    self.cogene_powerunit_PEFC = 'PEFC'
                    self.cogene_tankunit_PEFC = 'PEFC'
                    self.cogene_backupboiler_PEFC = 'PEFC'
                cogene_context += [
                    '発電ユニット（PEFC）：' + self.cogene_powerunit_PEFC,
                    '貯湯ユニット（PEFC）：' + self.cogene_tankunit_PEFC,
                    'バックアップボイラー（PEFC）：' + self.cogene_backupboiler_PEFC,
                    ]
            elif self.cogene_type == 'SOFC':
                if self.cogene_SOFC_input:
                    self.cogene_powerunit_SOFC = 'SOFC'
                    self.cogene_tankunit_SOFC = 'SOFC'
                    self.cogene_backupboiler_SOFC = 'SOFC'
                else:
                    self.cogene_powerunit_SOFC = 'SOFC'
                    self.cogene_tankunit_SOFC = 'SOFC'
                    self.cogene_backupboiler_SOFC = 'SOFC'
                cogene_context += [
                    '発電ユニット（SOFC）：' + self.cogene_powerunit_SOFC,
                    '貯湯ユニット（SOFC）：' + self.cogene_tankunit_SOFC,
                    'バックアップボイラー（SOFC）：' + self.cogene_backupboiler_SOFC,
                    ]
            else:
                cogene_context += [
                    'コージェネ発電ユニット（2015年以前の評価方法またはGEC）：' + self.get_cogene_unit_powerunit_2015_display(),
                    ]
        else:
            cogene_context = [
                'コージェネレーション設備を' + self.get_cogene_display(),
                ]
        return cogene_context

