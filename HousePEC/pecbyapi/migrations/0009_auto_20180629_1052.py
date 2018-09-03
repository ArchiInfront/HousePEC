# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pecbyapi', '0008_auto_20180628_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housespec',
            name='gasoil_water_heater_jis_efficiency',
        ),
        migrations.RemoveField(
            model_name='housespec',
            name='heating_water_heater_jis_efficiency',
        ),
        migrations.RemoveField(
            model_name='housespec',
            name='heatpump_water_heater_jis_efficiency',
        ),
        migrations.AddField(
            model_name='housespec',
            name='gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Mode',
            field=models.DecimalField(decimal_places=1, default=81.0, help_text='ガス従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のモード熱効率[%]を小数点以下1桁まで入力します。', max_digits=3, verbose_name='ガス従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のモード熱効率[%]'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Other',
            field=models.DecimalField(decimal_places=1, default=81.0, help_text='ガス従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のエネルギー消費効率[%]を小数点以下1桁まで入力します。', max_digits=3, verbose_name='ガス従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のエネルギー消費効率[%]'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Mode',
            field=models.DecimalField(decimal_places=1, default=87.0, help_text='ガス潜熱回収型給湯温水暖房機（給湯・温水暖房一体型）暖房部のモード熱効率[%]を小数点以下1桁まで入力します。', max_digits=3, verbose_name='ガス潜熱回収型給湯温水暖房機（給湯・温水暖房一体型）暖房部のモード熱効率[%]'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Other',
            field=models.DecimalField(decimal_places=1, default=87.0, help_text='ガス潜熱回収型給湯温水暖房機（給湯・温水暖房一体型）暖房部のエネルギー消費効率[%]を小数点以下1桁まで入力します。', max_digits=3, verbose_name='ガス潜熱回収型給湯温水暖房機（給湯・温水暖房一体型）暖房部のエネルギー消費効率[%]'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Mode',
            field=models.DecimalField(decimal_places=1, default=82.0, help_text='石油従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のモード熱効率[%]を小数点以下1桁まで入力します。', max_digits=3, verbose_name='石油従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のモード熱効率[%]'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Other',
            field=models.DecimalField(decimal_places=1, default=82.0, help_text='石油従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のエネルギー消費効率[%]を小数点以下1桁まで入力します。', max_digits=3, verbose_name='石油従来型給湯温水暖房機（給湯・温水暖房一体型）暖房部のエネルギー消費効率[%]'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='gasoil_water_heater_jis_efficiency_GasClassic_Mode',
            field=models.DecimalField(decimal_places=1, default=70.4, help_text='ガス従来型給湯機（給湯専用型）のモード熱効率[%]を小数点以下1桁まで入力します。', max_digits=3, verbose_name='ガス従来型給湯機のモード熱効率[%]'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='gasoil_water_heater_jis_efficiency_GasClassic_Other',
            field=models.DecimalField(decimal_places=1, default=70.4, help_text='ガス従来型給湯機（給湯専用型）のエネルギー消費効率[%]を小数点以下1桁まで入力します。', max_digits=3, verbose_name='ガス従来型給湯機のエネルギー消費効率[%]'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Mode',
            field=models.DecimalField(decimal_places=1, default=83.6, help_text='ガス潜熱回収型給湯機（給湯専用型）のモード熱効率[%]を小数点以下1桁まで入力します。', max_digits=3, verbose_name='ガス潜熱回収型給湯機のモード熱効率[%]）'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Other',
            field=models.DecimalField(decimal_places=1, default=83.6, help_text='ガス潜熱回収型給湯機（給湯専用型）のエネルギー消費効率[%]を小数点以下1桁まで入力します。', max_digits=3, verbose_name='ガス潜熱回収型給湯機のエネルギー消費効率[%]'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='gasoil_water_heater_jis_efficiency_OilClassic_Mode',
            field=models.DecimalField(decimal_places=1, default=77.9, help_text='石油従来型給湯機（給湯専用型）のモード熱効率[%]を小数点以下1桁まで入力します。', max_digits=3, verbose_name='石油従来型給湯機のモード熱効率[%]'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='gasoil_water_heater_jis_efficiency_OilClassic_Other',
            field=models.DecimalField(decimal_places=1, default=77.9, help_text='石油従来型給湯機（給湯専用型）の熱効率[%]を小数点以下1桁まで入力します。', max_digits=3, verbose_name='石油従来型給湯機の熱効率[%]'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Mode',
            field=models.DecimalField(decimal_places=1, default=81.9, help_text='石油潜熱回収型給湯機（給湯専用型）のモード熱効率[%]を小数点以下1桁まで入力します。', max_digits=3, verbose_name='石油潜熱回収型給湯機のモード熱効率[%]'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other',
            field=models.DecimalField(decimal_places=1, default=81.9, help_text='石油潜熱回収型給湯機（給湯専用型）の熱効率[%]を小数点以下1桁まで入力します。', max_digits=3, verbose_name='石油潜熱回収型給湯機の熱効率[%]'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='heatpump_water_heater_jis_efficiency_M1SEJISEfficiency',
            field=models.DecimalField(decimal_places=1, default=3.6, help_text='CO2冷媒電気ヒートポンプ給湯機（給湯専用型）のM1スタンダードに基づくJIS相当効率（認定機種限定）を小数点以下2桁まで入力します。', max_digits=2, verbose_name='M1スタンダードに基づくJIS相当効率（認定機種限定）'),
        ),
        migrations.AddField(
            model_name='housespec',
            name='heatpump_water_heater_jis_efficiency_Other',
            field=models.DecimalField(decimal_places=1, default=2.7, help_text='CO2冷媒電気ヒートポンプ給湯機（給湯専用型）のJIS効率[-]をは小数点以下1桁まで入力します。', max_digits=2, verbose_name='ヒートポンプのJIS効率[-]'),
        ),
        migrations.AlterField(
            model_name='housespec',
            name='gasoil_water_heater_efficiency_type',
            field=models.CharField(choices=[('Mode', 'モード熱効率'), ('Other', '熱効率またはエネルギー消費効率'), ('None', '効率を入力しない')], default='None', help_text='給湯機（もしくは給湯温水暖房機の給湯部）の効率の種類を指定します。\n        モード熱効率（燃料がガス・石油の場合）とは、JIS S 2075「家庭用ガス・石油温水機器のモード効率測定法」の測定方法による値です。\n        エネルギー消費効率（燃料がガスの場合）とは、旧省エネ法において定義される「エネルギー消費効率」（ガス温水機器）に相当します。\n        熱効率（燃料が石油の場合）とは、JIS S 3031「石油燃焼機器の試験方法通則」の連続給湯効率試験方法あるいは湯沸効率試験方法による値です。\n        ', max_length=17, verbose_name='給湯機効率種類（ガス・石油熱源の場合）'),
        ),
        migrations.AlterField(
            model_name='housespec',
            name='heatpump_water_heater_efficiency_type',
            field=models.CharField(choices=[('M1SEJISEfficiency', 'M1スタンダードに基づくJIS相当効率'), ('Other', 'JIS効率'), ('None', '効率を入力しない')], default='None', help_text='給湯機の効率の種類を指定します。\n        JIS効率とは、JIS C 9220（家庭用ヒートポンプ給湯機）による年間給湯保温効率（JIS）又は年間給湯効率（JIS）です。\n        M1スタンダードに基づくJIS相当効率は、2017年10月16日現在、株式会社コロナの機種に限定されます。\n        ', max_length=17, verbose_name='給湯機効率種類（ヒートポンプ熱源の場合）'),
        ),
    ]