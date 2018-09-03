from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.core.urlresolvers import reverse
#from django.forms import modelform_factory

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from django.http import JsonResponse
from django.utils import timezone

from pecbyapi.models import HouseBuilder, HouseBasic, HouseSpec
from pecbyapi.forms import NewHouseForm, NewHouseDetailForm, CopyHouseDetailForm, UpdateHouseForm, UpdateHouseDetailForm
from pecbyapi.forms import NewSpecForm, NewSpecDetailForm, UpdateSpecForm, CopySpecForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

# House
@login_required
def house_list(request, pk):
    builder = get_object_or_404(HouseBuilder, pk=pk)
    houses = HouseBasic.objects.filter(builder=builder)
    context = {'builder': builder, 'house':houses}
    return render(request, 'house_list.html', context)

@login_required
def house_list_detail(request, pk):
    builder = get_object_or_404(HouseBuilder, pk=pk)
    houses = HouseBasic.objects.filter(builder=builder)
    context = {'builder': builder, 'house':houses}
    return render(request, 'house_list_detail.html', context)

@login_required
def house_confirm_delete(request, pk, house_pk):
    builder = get_object_or_404(HouseBuilder, pk=pk)
    house = get_object_or_404(HouseBasic, builder__pk=pk, pk=house_pk)
    if request.method == 'POST':
        house.delete()
        return redirect('house_list', pk=builder.pk)
    return render(request, 'house_confirm_delete.html', {'builder':builder, 'house': house})

@login_required
def house_update(request, pk, house_pk):
    builder = get_object_or_404(HouseBuilder, pk=pk)
    house = get_object_or_404(HouseBasic, builder__pk=pk, pk=house_pk)
    if request.method == 'POST':
        form = UpdateHouseForm(request.POST, instance=house)
        if form.is_valid():
            house = form.save(commit=False)
            if house.nonldk_area_check():
                house.builder = builder
                house.save()
                return redirect('house_list', pk=builder.pk)
            else:
                messages.warning(request, "主居室と他居室の床面積の合計が、延床面積（主居室、他居室、非居室の合計）よりも大きく設定されています。※「非居室床面積＝延床面積－主居室面積－他居室面積」により計算されます。")
    else:
        form = UpdateHouseForm(instance=house)
    return render(request, 'house_update.html', {'form':form, 'builder':builder, 'house':house})

@login_required
def house_update_detail(request, pk, house_pk):
    builder = get_object_or_404(HouseBuilder, pk=pk)
    house = get_object_or_404(HouseBasic, builder__pk=pk, pk=house_pk)
    if request.method == 'POST':
        form = UpdateHouseDetailForm(request.POST, instance=house)
        if form.is_valid():
            house = form.save(commit=False)
            if house.nonldk_area_check():
                house.builder = builder
                house.save()
                return redirect('house_list', pk=builder.pk)
            else:
                messages.warning(request, "主居室と他居室の床面積の合計が、延床面積（主居室、他居室、非居室の合計）よりも大きく設定されています。※「非居室床面積＝延床面積－主居室面積－他居室面積」により計算されます。")
    else:
        form = UpdateHouseDetailForm(instance=house)
    return render(request, 'house_update_detail.html', {'form':form, 'builder':builder, 'house':house})

@login_required
def house_new(request, pk):
    builder = get_object_or_404(HouseBuilder, pk=pk)
    if request.method == 'POST':
        form = NewHouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            if house.nonldk_area_check():
                house.builder = builder
                house.save()
                return redirect('house_list', pk=builder.pk)
            else:
                messages.warning(request, "主居室と他居室の床面積の合計が、延床面積（主居室、他居室、非居室の合計）よりも大きく設定されています。※「非居室床面積＝延床面積－主居室面積－他居室面積」により計算されます。")
    else:
        form = NewHouseForm()
    return render(request, 'house_new.html', {'form':form, 'builder':builder})

@login_required
def house_new_detail(request, pk):
    builder = get_object_or_404(HouseBuilder, pk=pk)
    if request.method == 'POST':
        form = NewHouseDetailForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            if house.nonldk_area_check():
                house.builder = builder
                house.save()
                return redirect('house_list', pk=builder.pk)
            else:
                messages.warning(request, "主居室と他居室の床面積の合計が、延床面積（主居室、他居室、非居室の合計）よりも大きく設定されています。※「非居室床面積＝延床面積－主居室面積－他居室面積」により計算されます。")
    else:
        form = NewHouseDetailForm()
    return render(request, 'house_new_detail.html', {'form':form, 'builder':builder})

@login_required
def house_copy(request, pk, house_pk):
    builder = get_object_or_404(HouseBuilder, pk=pk)
    house = get_object_or_404(HouseBasic, builder__pk=pk, pk=house_pk)
    if request.method == 'POST':
        form = CopyHouseDetailForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            if house.nonldk_area_check():
                house.builder = builder
                house.save()
                return redirect('house_list', pk=builder.pk)
            else:
                messages.warning(request, "主居室と他居室の床面積の合計が、延床面積（主居室、他居室、非居室の合計）よりも大きく設定されています。※「非居室床面積＝延床面積－主居室面積－他居室面積」により計算されます。")
    else:
        form = CopyHouseDetailForm(instance=house)
    return render(request, 'house_copy.html', {'form':form, 'builder':builder, 'house':house})


# Spec
@login_required
def spec_list(request, pk, house_pk):
    builder = get_object_or_404(HouseBuilder, pk=pk)
    house = get_object_or_404(HouseBasic, builder__pk=pk, pk=house_pk)
    specs = HouseSpec.objects.filter(builder=builder).filter(house=house)
    calcs = HouseSpec.objects.filter(builder=builder).filter(house=house).filter(calc_done=False)
    context = {'builder': builder, 'house':house, 'specs':specs, 'calcs':calcs}
    return render(request, 'spec_list.html', context)

@login_required
def spec_new(request, pk, house_pk):
    builder = get_object_or_404(HouseBuilder, pk=pk)
    house = get_object_or_404(HouseBasic, builder__pk=pk, pk=house_pk)
    if request.method == 'POST':
        form = NewSpecForm(request.POST)
        if form.is_valid():
            spec = form.save(commit=False)
            spec.builder = builder
            spec.house = house
            spec.save()
            return redirect('spec_list', pk=pk, house_pk=house_pk)
    else:
        form = NewSpecForm()
    return render(request, 'spec_new.html', {'form':form, 'builder':builder, 'house':house})

@login_required
def spec_new_detail(request, pk, house_pk):
    builder = get_object_or_404(HouseBuilder, pk=pk)
    house = get_object_or_404(HouseBasic, builder__pk=pk, pk=house_pk)
    if request.method == 'POST':
        form = NewSpecForm(request.POST)
        if form.is_valid():
            spec = form.save(commit=False)
            spec.builder = builder
            spec.house = house
            spec.save()
            return redirect('spec_list', pk=pk, house_pk=house_pk)
    else:
        form = NewSpecForm()
    return render(request, 'spec_new.html', {'form':form, 'builder':builder, 'house':house})

@login_required
def spec_update(request, pk, house_pk, spec_pk):
    builder = get_object_or_404(HouseBuilder, pk=pk)
    house = get_object_or_404(HouseBasic, builder__pk=pk, pk=house_pk)
    spec = get_object_or_404(HouseSpec, builder__pk=pk, house__pk=house_pk, pk=spec_pk)
    if request.method == 'POST':
        form = UpdateSpecForm(request.POST, instance=spec)
        if form.is_valid():
            spec = form.save(commit=False)
            spec.builder = builder
            spec.house = house
            spec.calc_done = False
            spec.save()
            return redirect('spec_list', pk=pk, house_pk=house_pk)
    else:
        form = UpdateSpecForm(instance=spec)
    return render(request, 'spec_update.html', {'form':form, 'builder':builder, 'house':house, 'spec':spec})

@login_required
def spec_confirm_delete(request, pk, house_pk, spec_pk):
    builder = get_object_or_404(HouseBuilder, pk=pk)
    house = get_object_or_404(HouseBasic, builder__pk=pk, pk=house_pk)
    spec = get_object_or_404(HouseSpec, builder__pk=pk, house__pk=house_pk, pk=spec_pk)
    if request.method == 'POST':
        spec.delete()
        return redirect('spec_list', pk=pk, house_pk=house_pk)
    return render(request, 'spec_confirm_delete.html', {'builder':builder, 'house': house, 'spec':spec})

@login_required
def spec_copy(request, pk, house_pk, spec_pk):
    builder = get_object_or_404(HouseBuilder, pk=pk)
    house = get_object_or_404(HouseBasic, builder__pk=pk, pk=house_pk)
    spec = get_object_or_404(HouseSpec, builder__pk=pk, house__pk=house_pk, pk=spec_pk)
    if request.method == 'POST':
        form = CopySpecForm(request.POST)
        if form.is_valid():
            spec = form.save(commit=False)
            spec.builder = builder
            spec.house = house
            spec.calc_done = False
            spec.save()
            return redirect('spec_list', pk=pk, house_pk=house_pk)
    else:
        form = CopySpecForm(instance=spec)
    return render(request, 'spec_copy.html', {'form':form, 'builder':builder, 'house':house, 'spec':spec})

@login_required
def spec_calc(request, pk, house_pk):
    import sys
    from io import BytesIO
    import base64
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    builder = get_object_or_404(HouseBuilder, pk=pk)
    house = get_object_or_404(HouseBasic, builder__pk=pk, pk=house_pk)
    specs = HouseSpec.objects.filter(builder=builder).filter(house=house)
    calcs = HouseSpec.objects.filter(builder=builder).filter(house=house).filter(calc_done=False)

    if calcs:
        for spec in calcs:
            xml = makeXML(spec)
            data = {'ErrMessage':xml['ErrMessage'],
                    'Total':[xml['E_T']/1000, xml['E_ST']/1000, ],
                    'Lighting':[xml['E_L']/1000, xml['E_SL']/1000, ],
                    'Hotwater':[xml['E_W']/1000, xml['E_SW']/1000, ],
                    'Ventilation':[xml['E_V']/1000, xml['E_SV']/1000, ],
                    'Cooling':[xml['E_C']/1000, xml['E_SC']/1000, ],
                    'Heating':[xml['E_H']/1000, xml['E_SH']/1000, ],
                    'Other':[xml['E_M']/1000, xml['E_SM']/1000, ],
                    'ReduceByPV':xml['E_S']/1000,
                    'SellByPV':xml['E_PV_sell']/1000,
                    'GenerateByPV':xml['E_PV_gen']/1000,
                    'GenerateByCG':xml['E_CG_gen']/1000,
                    }
            df = pd.DataFrame(data)
            if data['ErrMessage'] == '':
                spec.resErrMessage = ''
                spec.resE_T = df['Total'][0]
                spec.resE_ST = df['Total'][1]
                spec.resE_L = df['Lighting'][0]
                spec.resE_SL = df['Lighting'][1]
                spec.resE_W = df['Hotwater'][0]
                spec.resE_SW = df['Hotwater'][1]
                spec.resE_V = df['Ventilation'][0]
                spec.resE_SV = df['Ventilation'][1]
                spec.resE_C = df['Cooling'][0]
                spec.resE_SC = df['Cooling'][1]
                spec.resE_H = df['Heating'][0]
                spec.resE_SH = df['Heating'][1]
                spec.resE_M = df['Other'][0]
                spec.resE_SM = df['Other'][1]
                spec.resReduceByPV = df['ReduceByPV'][0]
                spec.resSellByPV = df['SellByPV'][0]
                spec.resGenerateByPV = df['GenerateByPV'][0]
                spec.resGenerateByCG = df['GenerateByCG'][0]
                spec.calc_done = True
                spec.save()
            else:
                spec.resErrMessage = df['ErrMessage'][0]
                spec.calc_done = False
                spec.save()
    
    data_list = []
    if specs:
        for spec in specs:
            if spec.calc_done:
                data = {'Total':[spec.resE_T, spec.resE_ST, ],
                        'Lighting':[spec.resE_L, spec.resE_SL, ],
                        'Hotwater':[spec.resE_W, spec.resE_SW, ],
                        'Ventilation':[spec.resE_V, spec.resE_SV, ],
                        'Cooling':[spec.resE_C, spec.resE_SC, ],
                        'Heating':[spec.resE_H, spec.resE_SH, ],
                        'Other':[spec.resE_M, spec.resE_SM, ],
                        'ReduceByPV':spec.resReduceByPV,
                        'SellByPV':spec.resSellByPV,
                        'GenerateByPV':spec.resGenerateByPV,
                        'GenerateByCG':spec.resGenerateByCG,
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
                df['subTotal'] = df['Lighting'] + df['Hotwater'] + df['Ventilation'] + df['Cooling'] + df['Heating']
                df = df.round().astype(int)
                data = df.to_dict()
                data['fig'] = image_base64
                buf.close()
                plt.close('all')
                data_list.append(data)
            else:
                data = {'ErrMessage':spec.resErrMessage}
                data_list.append(data)
    else:
        pass

    context = {'builder': builder, 'house':house, 'specs':specs, 'calcs':calcs, 'data_list':data_list}
    return render(request, 'spec_calc.html', context)


def makeXML(i):
    import urllib.request, urllib.error, urllib.parse
    import xml.etree.ElementTree as ET

    #HouseBasic
    model  = '<House FileVer="1" Name="' + i.house.name + '" Type="Standard,Independent" TotalArea="' + str(i.house.total_area) + '">'
    model += '<Environment Region="' + str(i.house.region) + '" AnnualSolarLevel="' + i.house.annual_solar_level + '" />'
    model += '<Zones>'
    model += '<Zone Type="LDK" Area="' + str(i.house.ldk_area) + '" NaturalWind="' + str(i.house.ldk_natural_wind) + '" />'
    model += '<Zone Type="Other" Area="' + str(i.house.ldk_area) + '" NaturalWind="' + str(i.house.oth_natural_wind) + '" />'
    model += '</Zones>'
    model += '<Envelope HeatStorage="' + i.house.heat_storage + '" EvaluationMethod="Real" TotalEnvelopeArea="' + str(i.house.total_envelope_area) + '" UAValue="' + str(i.house.ua_value) + '" SummerHAValue="' + str(i.house.summer_ha_value) + '" WinterHAValue="' + str(i.house.winter_ha_value) + '" />'
        
    #Heating
    if i.heating_system == 'RoomSpaceHeating':
        model += '<Heating Type="Individual">'
        if i.ldk_heating_type == 'RoomAirConditioningHeating':
            model += '<RoomAirConditioningHeating Zone="LDK" Efficiency="' + i.ldk_ac_heating_efficiency + '" Compressor="' + i.ldk_ac_heating_compressor + '" />'
        elif i.ldk_heating_type == 'FFHeating':
            if i.ldk_ff_saving_input:
                model += '<FFHeating Zone="LDK" Efficiency="' + str(i.ldk_ff_heating_efficiency) + '" />'
            else:
                model += '<FFHeating Zone="LDK" />'
        elif i.ldk_heating_type in ['PanelRadiator', 'HotWaterFloorHeatingRadiator', 'FanConvectorRadiator', ]:
            if i.ldk_heating_type == 'HotWaterFloorHeatingRadiator':
                model += '<HotWaterFloorHeatingRadiator Zone="LDK" AreaRate="' + str(i.ldk_hotwater_floorheating_area_rate) + '"  UpwardHeatFlowRate="' + str(i.ldk_hotwater_floorheating_upward_heatflow_rate) + '"/>'
            else:
                model += '<' + i.ldk_heating_type + ' Zone="LDK" />'

            if i.hotwater_heating_system == 'NonIntegrated':
                if i.hotwater_heating_source_type in ['OilClassic', 'GasClassic', 'GasLatentHeatRecovery', ]:
                    if i.hotwater_heating_source_saving_input:
                        if i.hotwater_heating_source_type == 'OilClassic':
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Efficiency="' + str(i.hotwater_heating_source_efficiency_OilClassic) + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                        elif i.hotwater_heating_source_type == 'GasClassic':
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Efficiency="' + str(i.hotwater_heating_source_efficiency_GasClassic) + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                        elif i.hotwater_heating_source_type == 'GasLatentHeatRecovery':
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Efficiency="' + str(i.hotwater_heating_source_efficiency_GasLatentHeatRecovery) + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                        else:
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                    else:
                        model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                elif i.hotwater_heating_source_type in ['OilLatentHeatRecovery', 'ElectricHeatPump', 'ElectricHeater', ]:
                    model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                else:
                    model += '<HotwaterHeatSource Type="NotUsed" Pipe="' + i.hotwater_heating_source_pipe + '" />'
            elif i.hotwater_heating_system in ['Integrated', 'Cogeneration', ]:
                model += '<HotwaterHeatSource Type="' + i.hotwater_heating_system + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
            elif i.hotwater_heating_system == 'Other':
                model += '<HotwaterHeatSource Name="' + i.hotwater_heating_source_name + '" Type="Other" Pipe="' + i.hotwater_heating_source_pipe + '" />'
            else:
                model += '<HotwaterHeatSource Type="NotUsed" Pipe="' + i.hotwater_heating_source_pipe + '" />'
        elif i.ldk_heating_type == 'ElecricFloorHeating':
            model += '<ElecricFloorHeating Zone="LDK" AreaRate="' + str(i.ldk_elecric_floorheating_area_rate) + '"  UpwardHeatFlowRate="' + str(i.ldk_elecric_floorheating_upward_heatflow_rate) + '"/>'
        elif i.ldk_heating_type == 'ElectricRoomHeaterWithThermalStorage':
            model += '<ElectricRoomHeaterWithThermalStorage Zone="LDK" />'
        elif i.ldk_heating_type == 'FloorHeatingWithRAC':
            model += '<FloorHeatingWithRAC Zone="LDK" AreaRate="' + str(i.ldk_ac_floorheating_area_rate) + '"  UpwardHeatFlowRate="' + str(i.ldk_ac_floorheating_upward_heatflow_rate) + '" Pipe="' + i.ldk_ac_floorheating_pipe + '" />'
        elif i.ldk_heating_type == 'OtherHeatingDevice':
            model += '<OtherHeatingDevice Zone="LDK" Name="' + i.ldk_other_heating_device_name + '" />'
        else:
            model += '<NotInstalled Zone="LDK" />'

        if i.oth_heating_type == 'RoomAirConditioningHeating':
            model += '<RoomAirConditioningHeating Zone="Other" Efficiency="' + i.oth_ac_heating_efficiency + '" Compressor="' + i.oth_ac_heating_compressor + '" />'
        elif i.oth_heating_type == 'FFHeating':
            if i.oth_ff_saving_input:
                model += '<FFHeating Zone="Other" Efficiency="' + str(i.oth_ff_heating_efficiency) + '" />'
            else:
                model += '<FFHeating Zone="Other" />'
        elif i.oth_heating_type in ['PanelRadiator', 'HotWaterFloorHeatingRadiator', 'FanConvectorRadiator', ]:
            if i.oth_heating_type == 'HotWaterFloorHeatingRadiator':
                model += '<HotWaterFloorHeatingRadiator Zone="Other" AreaRate="' + str(i.oth_hotwater_floorheating_area_rate) + '"  UpwardHeatFlowRate="' + str(i.oth_hotwater_floorheating_upward_heatflow_rate) + '"/>'
            else:
                model += '<' + i.oth_heating_type + ' Zone="Other" />'

            if i.hotwater_heating_system == 'NonIntegrated':
                if i.hotwater_heating_source_type in ['OilClassic', 'GasClassic', 'GasLatentHeatRecovery', ]:
                    if i.hotwater_heating_source_saving_input:
                        if i.hotwater_heating_source_type == 'OilClassic':
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Efficiency="' + str(i.hotwater_heating_source_efficiency_OilClassic) + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                        elif i.hotwater_heating_source_type == 'GasClassic':
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Efficiency="' + str(i.hotwater_heating_source_efficiency_GasClassic) + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                        elif i.hotwater_heating_source_type == 'GasLatentHeatRecovery':
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Efficiency="' + str(i.hotwater_heating_source_efficiency_GasLatentHeatRecovery) + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                        else:
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                    else:
                        model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                elif i.hotwater_heating_source_type in ['OilLatentHeatRecovery', 'ElectricHeatPump', 'ElectricHeater', ]:
                    model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                else:
                    model += '<HotwaterHeatSource Type="NotUsed" Pipe="' + i.hotwater_heating_source_pipe + '" />'
            elif i.hotwater_heating_system in ['Integrated', 'Cogeneration', ]:
                model += '<HotwaterHeatSource Type="' + i.hotwater_heating_system + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
            elif i.hotwater_heating_system == 'Other':
                model += '<HotwaterHeatSource Name="' + i.hotwater_heating_source_name + '" Type="Other" Pipe="' + i.hotwater_heating_source_pipe + '" />'
            else:
                model += '<HotwaterHeatSource Type="NotUsed" Pipe="' + i.hotwater_heating_source_pipe + '" />'
        elif i.oth_heating_type == 'ElecricFloorHeating':
            model += '<ElecricFloorHeating Zone="Other" AreaRate="' + str(i.oth_elecric_floorheating_area_rate) + '"  UpwardHeatFlowRate="' + str(i.oth_elecric_floorheating_upward_heatflow_rate) + '"/>'
        elif i.oth_heating_type == 'ElectricRoomHeaterWithThermalStorage':
            model += '<ElectricRoomHeaterWithThermalStorage Zone="Other" />'
        elif i.oth_heating_type == 'FloorHeatingWithRAC':
            model += '<FloorHeatingWithRAC Zone="Other" AreaRate="' + str(i.oth_ac_floorheating_area_rate) + '"  UpwardHeatFlowRate="' + str(i.oth_ac_floorheating_upward_heatflow_rate) + '" Pipe="' + i.oth_ac_floorheating_pipe + '" />'
        elif i.oth_heating_type == 'OtherHeatingDevice':
            model += '<OtherHeatingDevice Zone="Other" Name="' + i.oth_other_heating_device_name + '" />'
        else:
            model += '<NotInstalled Zone="Other" />'
    elif i.heating_system == 'AllSpaceHeating':
        model += '<Heating Type="Central">'
        if i.heating_rated_input:
            model += '<ElectricHeatPumpCentralHeating RatedPower="' + str(i.heating_rated_power) + '" RatedCapacity="' + str(i.heating_rated_capacity) + '" PowerCorrection="' + i.heating_power_correction + '" Coefficient="' + str(i.heating_coefficient) + '" />'
        else:
            model += '<ElectricHeatPumpCentralHeating PowerCorrection="' + i.heating_power_correction + '" Coefficient="' + str(i.heating_coefficient) + '" />'
    else:
        model += '<Heating Type="NotInstalled">'
    model += '</Heating>'

    #Cooling
    if i.cooling_system == 'RoomSpaceCooling':
        model += '<Cooling Type="Individual">'
        if i.ldk_cooling_type == 'RoomAirConditioningCooling':
            model += '<RoomAirConditioningCooling Zone="LDK" Efficiency="' + i.ldk_ac_cooling_efficiency + '" Compressor="' + i.ldk_ac_cooling_compressor + '" />'
        elif i.ldk_cooling_type == 'OtherCoolingDevice':
            model += '<OtherCoolingDevice Zone="LDK" Name="' + i.ldk_other_cooling_device_name + '" />'
        else:
            model += '<NotInstalled Zone="LDK" />'

        if i.oth_cooling_type == 'RoomAirConditioningCooling':
            model += '<RoomAirConditioningCooling Zone="Other" Efficiency="' + i.oth_ac_cooling_efficiency + '" Compressor="' + i.oth_ac_cooling_compressor + '" />'
        elif i.oth_cooling_type == 'OtherCoolingDevice':
            model += '<OtherCoolingDevice Zone="Other" Name="' + i.oth_other_cooling_device_name + '" />'
        else:
            model += '<NotInstalled Zone="Other" />'
    elif i.cooling_system == 'AllSpaceCooling':
        model += '<Cooling Type="Central">'
        if i.cooling_rated_input:
            model += '<ElectricHeatPumpCentralCooling RatedPower="' + str(i.cooling_rated_power) + '" RatedCapacity="' + str(i.cooling_rated_capacity) + '" PowerCorrection="' + i.cooling_power_correction + '" Coefficient="' + str(i.cooling_coefficient) + '" />'
        else:
            model += '<ElectricHeatPumpCentralCooling PowerCorrection="' + i.cooling_power_correction + '" Coefficient="' + str(i.cooling_coefficient) + '" />'
    else:
        model += '<Cooling Type="NotInstalled">'
    model += '</Cooling>'
    
    #Ventilation
    #model += '<Ventilation Type="DuctVentilation1" Saving="ThickDuctAndDCMotor" HeatExchanger="HeatExchanger" Frequency="HalfPerHour" Efficiency="0.95" HeatExchangerEfficiency="80" HeatExchangerLeak="1.00" HeatExchangerBal="0.90" />'
    #model += '''<Ventilation Type="DuctVentilation1" Saving="''' + i.ventilation_saving +'''" HeatExchanger="HeatExchanger" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" HeatExchangerEfficiency="'''+ str(i.ventilation_heatexchanger_efficiency) +'''" HeatExchangerLeak="'''+ str(i.ventilation_heatexchanger_leak) +'''" HeatExchangerBal="'''+ str(i.ventilation_heatexchanger_bal) +'''" />'''

    if i.ventilation_type == 'DuctVenitlation1':
        if i.ventilation_heatexchanger == 'HeatExchanger':
            if i.ventilation_saving in ['ThickDuctOnly', 'ThickDuctAndDCMotor', ]:
                model += '''<Ventilation Type="DuctVentilation1" Saving="''' + i.ventilation_saving +'''" HeatExchanger="HeatExchanger" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" HeatExchangerEfficiency="'''+ str(i.ventilation_heatexchanger_efficiency) +'''" HeatExchangerLeak="'''+ str(i.ventilation_heatexchanger_leak) +'''" HeatExchangerBal="'''+ str(i.ventilation_heatexchanger_bal) +'''" />'''
            elif i.ventilation_saving == 'SFP':
                model += '''<Ventilation Type="DuctVentilation1" SFP="''' + str(i.ventilation_sfp) + '''" HeatExchanger="HeatExchanger" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" HeatExchangerEfficiency="'''+ str(i.ventilation_heatexchanger_efficiency) +'''" HeatExchangerLeak="'''+ str(i.ventilation_heatexchanger_leak) +'''" HeatExchangerBal="'''+ str(i.ventilation_heatexchanger_bal) +'''" />'''
            else:
                model += '''<Ventilation Type="DuctVentilation1" HeatExchanger="HeatExchanger" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" HeatExchangerEfficiency="'''+ str(i.ventilation_heatexchanger_efficiency) +'''" HeatExchangerLeak="'''+ str(i.ventilation_heatexchanger_leak) +'''" HeatExchangerBal="'''+ str(i.ventilation_heatexchanger_bal) +'''" />'''
        else:
            if i.ventilation_saving in ['ThickDuctOnly', 'ThickDuctAndDCMotor', ]:
                model += '''<Ventilation Type="DuctVentilation1" Saving="''' + i.ventilation_saving +'''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" />'''
            elif i.ventilation_saving == 'SFP':
                model += '''<Ventilation Type="DuctVentilation1" SFP="''' + str(i.ventilation_sfp) + '''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" />'''
            else:
                model += '''<Ventilation Type="DuctVentilation1" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" />'''
    elif i.ventilation_type == 'DuctVentilation2or3':
        if i.ventilation_saving in ['ThickDuctOnly', 'ThickDuctAndDCMotor', ]:
            model += '''<Ventilation Type="''' + i.ventilation_type + '''" Saving="''' + i.ventilation_saving + '''" HeatExchanger="None" Frequency="''' + i.ventilation_frequency + '''" Efficiency="1" />'''
        elif i.ventilation_saving == 'SFP':
            model += '''<Ventilation Type="'''+ i.ventilation_type + '''" SFP="'''+ str(i.ventilation_sfp) + '''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency + '''" Efficiency="1" />'''
        else:
            model += '''<Ventilation Type="'''+ i.ventilation_type + '''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency + '''" Efficiency="1" />'''
    elif i.ventilation_type == 'WallMount1':
        if i.ventilation_heatexchanger == 'HeatExchanger':
            if i.ventilation_saving == 'SFP':
                model += '''<Ventilation Type="'''+ i.ventilation_type + '''" SFP="'''+ str(i.ventilation_sfp) + '''" HeatExchanger="HeatExchanger" Frequency="'''+ i.ventilation_frequency + '''" Efficiency="'''+ str(i.ventilation_efficiency) + '''" HeatExchangerEfficiency="'''+ str(i.ventilation_heatexchanger_efficiency) + '''" HeatExchangerLeak="'''+ str(i.ventilation_heatexchanger_leak) + '''" HeatExchangerBal="'''+ str(i.ventilation_heatexchanger_bal) +'''" />'''
            else:
                model += '''<Ventilation Type="'''+ i.ventilation_type + '''" HeatExchanger="HeatExchanger" Frequency="'''+ i.ventilation_frequency + '''" Efficiency="'''+ str(i.ventilation_efficiency) + '''" HeatExchangerEfficiency="'''+ str(i.ventilation_heatexchanger_efficiency) + '''" HeatExchangerLeak="'''+ str(i.ventilation_heatexchanger_leak) +'''" HeatExchangerBal="'''+ str(i.ventilation_heatexchanger_bal) + '''" />'''
        else:
            if i.ventilation_saving == 'SFP':
                model += '''<Ventilation Type="'''+ i.ventilation_type +'''" SFP="'''+ str(i.ventilation_sfp) +'''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" />'''
            else:
                model += '''<Ventilation Type="'''+ i.ventilation_type +'''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" />'''
    elif i.ventilation_type == 'WallMount2or3':
        if i.ventilation_saving == 'SFP':
            model += '''<Ventilation Type="'''+ i.ventilation_type +'''" SFP="'''+ str(i.ventilation_sfp) +'''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="1" />'''
        else:
            model += '''<Ventilation Type="'''+ i.ventilation_type +'''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="1" />'''
    else:
        if i.ventilation_saving in ['ThickDuctOnly', 'ThickDuctAndDCMotor', ]:
            model += '''<Ventilation Type="'''+ i.ventilation_type +'''" Saving="'''+ i.ventilation_saving +'''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="1" />'''
        elif i.ventilation_saving == 'SFP':
            model += '''<Ventilation Type="'''+ i.ventilation_type +'''" SFP="'''+ str(i.ventilation_sfp) +'''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency + '''" Efficiency="1" />'''
        else:
            model += '''<Ventilation Type="'''+ i.ventilation_type + '''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency + '''" Efficiency="1" />'''
    
    #Hotwater
    if i.bathroom in ['TapAndBath', 'TapOnly']:
        model += '<Hotwater>'
        if i.hotwater_heating_system == 'NonIntegrated':
            if i.water_heater_type == 'GasClassic':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="GasClassic" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasClassic_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="GasClassic" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasClassic_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="GasClassic" />'
            elif i.water_heater_type == 'GasLatentHeatRecovery':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="GasLatentHeatRecovery" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="GasLatentHeatRecovery" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="GasLatentHeatRecovery" />'
            elif i.water_heater_type == 'OilClassic':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="OilClassic" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilClassic_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="OilClassic" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilClassic_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="OilClassic" />'
            elif i.water_heater_type == 'OilLatentHeatRecovery':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="OilLatentHeatRecovery" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="OilLatentHeatRecovery" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="OilLatentHeatRecovery" />'
            elif i.water_heater_type == 'ElectricHeatPump':
                if i.heatpump_water_heater_efficiency_type == 'M1SEJISEfficiency':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="ElectricHeatPump" Name="'+ i.water_heater_name +'" EfficiencyType="M1SEJISEfficiency" JISEfficiency="'+ str(i.heatpump_water_heater_jis_efficiency_M1SEJISEfficiency) +'" />'
                elif i.heatpump_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="ElectricHeatPump" EfficiencyType="Other" JISEfficiency="'+ str(i.heatpump_water_heater_jis_efficiency_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="ElectricHeatPump" />'
            elif i.water_heater_type == 'Hybrid':
                if i.water_heater_heatpump_unit_input:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="Hybrid" HeatPumpUnit="RHP-R222(E)" TankUnit="RTU-R505(E)-U" BackupBoiler="RHBF-RK205SAT" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="Hybrid" HeatPumpUnit="'+ i.water_heater_heatpump_unit_coolant +'" TankCapacity="'+ i.water_heater_tank_capacity +'" />'
            elif i.water_heater_type == 'ElectricHeater':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="ElectricHeater" />'
            elif i.water_heater_type == 'Cogeneration':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="Cogeneration" />'
            elif i.water_heater_type == 'Other':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="Other" />'
            else:
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="NotUsed" />'
        elif i.hotwater_heating_system == 'Integrated':
            if i.integrated_water_heater_type == 'IntegratedGasClassic':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedGasClassic" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasClassic_Mode) +'" HeatingJISEfficiency="'+ str(i.gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedGasClassic" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasClassic_Other) +'" HeatingJISEfficiency="'+ str(i.gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedGasClassic" EfficiencyType="None" />'
            elif i.integrated_water_heater_type == 'IntegratedGasLatentHeatRecovery':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedGasLatentHeatRecovery" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Mode) +'" HeatingJISEfficiency="'+ str(i.gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedGasLatentHeatRecovery" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Other) +'" HeatingJISEfficiency="'+ str(i.gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedGasLatentHeatRecovery" EfficiencyType="None" />'
            elif i.integrated_water_heater_type == 'IntegratedOil':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedOil" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilClassic_Mode) +'" HeatingJISEfficiency="'+ str(i.gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedOil" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilClassic_Other) +'" HeatingJISEfficiency="'+ str(i.gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedOil" EfficiencyType="None" />'
            elif i.integrated_water_heater_type == 'IntegratedOilLatentHeatRecovery':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedOilLatentHeatRecovery" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedOilLatentHeatRecovery" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedOilLatentHeatRecovery" EfficiencyType="None" />'
            elif i.integrated_water_heater_type == 'Hybrid_Gas':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="Hybrid_Gas" TankPlace="'+ i.water_heater_tank_place +'" />'
            elif i.integrated_water_heater_type == 'Hybrid_Hybrid':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="Hybrid_Hybrid" />'
            elif i.integrated_water_heater_type == 'Gas_Hybrid':
                if i.water_heater_heatpump_unit_input:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="Gas_Hybrid" HeatPumpUnit="RHP-R222(E)" TankUnit="RTU-R505(E)-U" BackupBoiler="RHBF-RK205SAT" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="Gas_Hybrid" HeatPumpUnit="'+ i.water_heater_heatpump_unit_coolant +'" TankCapacity="'+ i.water_heater_tank_capacity +'" />'
            elif i.integrated_water_heater_type == 'IntegratedElectricHeater':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedElectricHeater" />'
            elif i.integrated_water_heater_type == 'Cogeneration':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="Cogeneration" />'
            elif i.integrated_water_heater_type == 'Other':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="Other" />'
            else:
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="NotUsed" />'
        elif i.hotwater_heating_system == 'Cogeneration':
            model += '<WaterHeater Install="'+ i.bathroom +'" Type="Cogeneration" />'
        elif i.hotwater_heating_system == 'Other':
            model += '<WaterHeater Install="'+ i.bathroom +'" Type="Other" Name="'+ i.water_heater_name +'" />'
        else:
            model += '<WaterHeater Install="'+ i.bathroom +'" Type="NotUsed" />'

        #model += '<WaterHeater Install="TapAndBath" Type="IntegratedOilLatentHeatRecovery" EfficiencyType="Other" JISEfficiency="95" />'
        model += '<Bath Function="'+ i.bath_function +'" Insulation="'+ i.bath_insulation +'" />'
        model += '<Pipe Type="'+ i.pipe_type +'" Saving="'+ i.pipe_saving +'" />'

        if i.bathroom == 'TapAndBath':
            model += '<Tap Type="BathShower" Saving="'+ i.bath_shower_tap_saving +'" />'
            model += '<Tap Type="Kitchen" Saving="'+ i.kitchen_tap_saving +'" />'
            model += '<Tap Type="WashBowl" Saving="'+ i.wash_bowl_tap_saving +'" />'
        elif i.bathroom == 'TapOnly':
            model += '<Tap Type="Kitchen" Saving="'+ i.kitchen_tap_saving +'" />'
            model += '<Tap Type="WashBowl" Saving="'+ i.wash_bowl_tap_saving +'" />'
        else:
            pass

        model += '</Hotwater>'
    else:
        pass


    #Lighting
    model += '<Lighting>'
    if i.ldk_lighting == 'HighEfficiency':
        if i.ldk_multi == 'Multi':
            if i.ldk_dimming == 'Dimming':
                model += '<LightingZone Zone="MainZone" Efficiency="HighEfficiency" Multi="Multi" Dimming="Dimming" />'
            else:
                model += '<LightingZone Zone="MainZone" Efficiency="HighEfficiency" Multi="Multi" Dimming="None" />'
        else:
            if i.ldk_dimming == 'Dimming':
                model += '<LightingZone Zone="MainZone" Efficiency="HighEfficiency" Multi="Single" Dimming="Dimming" />'
            else:
                model += '<LightingZone Zone="MainZone" Efficiency="HighEfficiency" Multi="Single" Dimming="None" />'
    elif i.ldk_lighting == 'LED':
        if i.ldk_multi == 'Multi':
            if i.ldk_dimming == 'Dimming':
                model += '<LightingZone Zone="MainZone" Efficiency="LED" Multi="Multi" Dimming="Dimming" />'
            else:
                model += '<LightingZone Zone="MainZone" Efficiency="LED" Multi="Multi" Dimming="None" />'
        else:
            if i.ldk_dimming == 'Dimming':
                model += '<LightingZone Zone="MainZone" Efficiency="LED" Multi="Single" Dimming="Dimming" />'
            else:
                model += '<LightingZone Zone="MainZone" Efficiency="LED" Multi="Single" Dimming="None" />'
    else:
        if i.ldk_multi == 'Multi':
            if i.ldk_dimming == 'Dimming':
                model += '<LightingZone Zone="MainZone" Efficiency="LowEfficiency" Multi="Multi" Dimming="Dimming" />'
            else:
                model += '<LightingZone Zone="MainZone" Efficiency="LowEfficiency" Multi="Multi" Dimming="None" />'
        else:
            if i.ldk_dimming == 'Dimming':
                model += '<LightingZone Zone="MainZone" Efficiency="LowEfficiency" Multi="Single" Dimming="Dimming" />'
            else:
                model += '<LightingZone Zone="MainZone" Efficiency="LowEfficiency" Multi="Single" Dimming="None" />'

    if i.oth_lighting == 'HighEfficiency':
        if i.oth_dimming == 'Dimming':
            model += '<LightingZone Zone="OtherZone" Efficiency="HighEfficiency" Dimming="Dimming" />'
        else:
            model += '<LightingZone Zone="OtherZone" Efficiency="HighEfficiency" Dimming="None" />'
    elif i.oth_lighting == 'LED':
        if i.oth_dimming == 'Dimming':
            model += '<LightingZone Zone="OtherZone" Efficiency="LED" Dimming="Dimming" />'
        else:
            model += '<LightingZone Zone="OtherZone" Efficiency="LED" Dimming="None" />'
    else:
        if i.oth_dimming == 'Dimming':
            model += '<LightingZone Zone="OtherZone" Efficiency="LowEfficiency" Dimming="Dimming" />'
        else:
            model += '<LightingZone Zone="OtherZone" Efficiency="LowEfficiency" Dimming="None" />'

    if i.nonldk_lighting == 'HighEfficiency':
        if i.nonldk_sensor == 'Sensor':
            model += '<LightingZone Zone="NonLivingZone" Efficiency="HighEfficiency" Sensor="Sensor" />'
        else:
            model += '<LightingZone Zone="NonLivingZone" Efficiency="HighEfficiency" Sensor="None" />'
    elif i.nonldk_lighting == 'LED':
        if i.nonldk_sensor == 'Sensor':
            model += '<LightingZone Zone="NonLivingZone" Efficiency="LED" Sensor="Sensor" />'
        else:
            model += '<LightingZone Zone="NonLivingZone" Efficiency="LED" Sensor="None" />'
    else:
        if i.nonldk_sensor == 'Sensor':
            model += '<LightingZone Zone="NonLivingZone" Efficiency="LowEfficiency" Sensor="Sensor" />'
        else:
            model += '<LightingZone Zone="NonLivingZone" Efficiency="LowEfficiency" Sensor="None" />'

    model += '</Lighting>'

    #Photovoltaic
    if i.photovoltaic in ['Panel1', 'Panel2', 'Panel3', 'Panel4']:
        if i.photovoltaic_power_conditioner_efficiency_input:
            model += '''<Photovoltaic PowerConditionerEfficiency="''' + str(i.photovoltaic_power_conditioner_efficiency) + '''">'''
        if i.photovoltaic == 'Panel1':
            model += '''<PhotovoltaicPanel Capacity="''' + str(i.photovol_panel_1_capacity) + '''" Cell="''' + i.photovoltaic_panel_1_cell + '''" Setup="''' + i.photovol_panel_1_setup + '''" Direction="''' + i.photovol_panel_1_direction + '''" Angle="''' + str(i.photovol_panel_1_angle) + '''" />'''
        elif i.photovoltaic == 'Panel2':
            model += '''<PhotovoltaicPanel Capacity="''' + str(i.photovol_panel_1_capacity) + '''" Cell="''' + i.photovoltaic_panel_1_cell + '''" Setup="''' + i.photovol_panel_1_setup + '''" Direction="''' + i.photovol_panel_1_direction + '''" Angle="''' + str(i.photovol_panel_1_angle) + '''" />'''
            model += '''<PhotovoltaicPanel Capacity="''' + str(i.photovol_panel_2_capacity) + '''" Cell="''' + i.photovoltaic_panel_2_cell + '''" Setup="''' + i.photovol_panel_2_setup + '''" Direction="''' + i.photovol_panel_2_direction + '''" Angle="''' + str(i.photovol_panel_2_angle) + '''" />'''
        elif i.photovoltaic == 'Panel3':
            model += '''<PhotovoltaicPanel Capacity="''' + str(i.photovol_panel_1_capacity) + '''" Cell="''' + i.photovoltaic_panel_1_cell + '''" Setup="''' + i.photovol_panel_1_setup + '''" Direction="''' + i.photovol_panel_1_direction + '''" Angle="''' + str(i.photovol_panel_1_angle) + '''" />'''
            model += '''<PhotovoltaicPanel Capacity="''' + str(i.photovol_panel_2_capacity) + '''" Cell="''' + i.photovoltaic_panel_2_cell + '''" Setup="''' + i.photovol_panel_2_setup + '''" Direction="''' + i.photovol_panel_2_direction + '''" Angle="''' + str(i.photovol_panel_2_angle) + '''" />'''
            model += '''<PhotovoltaicPanel Capacity="''' + str(i.photovol_panel_3_capacity) + '''" Cell="''' + i.photovoltaic_panel_3_cell + '''" Setup="''' + i.photovol_panel_3_setup + '''" Direction="''' + i.photovol_panel_3_direction + '''" Angle="''' + str(i.photovol_panel_3_angle) + '''" />'''
        elif i.photovoltaic == 'Panel4':
            model += '''<PhotovoltaicPanel Capacity="''' + str(i.photovol_panel_1_capacity) + '''" Cell="''' + i.photovoltaic_panel_1_cell + '''" Setup="''' + i.photovol_panel_1_setup + '''" Direction="''' + i.photovol_panel_1_direction + '''" Angle="''' + str(i.photovol_panel_1_angle) + '''" />'''
            model += '''<PhotovoltaicPanel Capacity="''' + str(i.photovol_panel_2_capacity) + '''" Cell="''' + i.photovoltaic_panel_2_cell + '''" Setup="''' + i.photovol_panel_2_setup + '''" Direction="''' + i.photovol_panel_2_direction + '''" Angle="''' + str(i.photovol_panel_2_angle) + '''" />'''
            model += '''<PhotovoltaicPanel Capacity="''' + str(i.photovol_panel_3_capacity) + '''" Cell="''' + i.photovoltaic_panel_3_cell + '''" Setup="''' + i.photovol_panel_3_setup + '''" Direction="''' + i.photovol_panel_3_direction + '''" Angle="''' + str(i.photovol_panel_3_angle) + '''" />'''
            model += '''<PhotovoltaicPanel Capacity="''' + str(i.photovol_panel_4_capacity) + '''" Cell="''' + i.photovoltaic_panel_4_cell + '''" Setup="''' + i.photovol_panel_4_setup + '''" Direction="''' + i.photovol_panel_4_direction + '''" Angle="''' + str(i.photovol_panel_4_angle) + '''" />'''
        model += '</Photovoltaic>'
    else:
        pass
    
    model += '</House>'

    ################################################################
    data = "<request><model>{}</model></request>".format(model)
    data = data.encode('utf-8')

    req = urllib.request.Request('http://house.app.lowenergy.jp/api/v1/eval', data=data)
    req.add_header('Content-type', 'application/xml; charset=utf-8')
    req.add_header('Accept', 'application/xml')
    res = urllib.request.urlopen(req)
    xml = res.read()

    if format(ET.fromstring(xml).findtext('error')) == 'None':
        ErrMessage = ''
        E_T = float(format(ET.fromstring(xml).findtext('E_T')))
        E_ST = float(format(ET.fromstring(xml).findtext('E_ST')))
        E_L = float(format(ET.fromstring(xml).findtext('E_L')))
        E_W = float(format(ET.fromstring(xml).findtext('E_W')))
        E_V = float(format(ET.fromstring(xml).findtext('E_V')))
        E_C = float(format(ET.fromstring(xml).findtext('E_C')))
        E_H = float(format(ET.fromstring(xml).findtext('E_H')))
        E_SL = float(format(ET.fromstring(xml).findtext('E_SL')))
        E_SW = float(format(ET.fromstring(xml).findtext('E_SW')))
        E_SV = float(format(ET.fromstring(xml).findtext('E_SV')))
        E_SC = float(format(ET.fromstring(xml).findtext('E_SC')))
        E_SH = float(format(ET.fromstring(xml).findtext('E_SH')))
        E_M = float(format(ET.fromstring(xml).findtext('E_M')))
        E_SM = float(format(ET.fromstring(xml).findtext('E_SM')))

        if format(ET.fromstring(xml).findtext('E_S')) == 'None':
            E_S = 0
        else:
            E_S = float(format(ET.fromstring(xml).findtext('E_S')))

        if format(ET.fromstring(xml).findtext('E_PV_sell')) == 'None':
            E_PV_sell = 0
        else:
            E_PV_sell = float(format(ET.fromstring(xml).findtext('E_PV_sell')))

        if format(ET.fromstring(xml).findtext('E_PV_gen')) == 'None':
            E_PV_gen = 0
        else:
            E_PV_gen = float(format(ET.fromstring(xml).findtext('E_PV_gen')))

        if format(ET.fromstring(xml).findtext('E_CG_gen')) == 'None':
            E_CG_gen = 0
        else:
            E_CG_gen = float(format(ET.fromstring(xml).findtext('E_CG_gen')))
    else:
        ErrMessage = format(ET.fromstring(xml).findtext('error'))
        E_T, E_ST, E_L, E_W, E_V, E_C, E_H, E_SL, E_SW, E_SV, E_SC, E_SH, E_S, E_M, E_SM, E_PV_sell, E_PV_gen, E_CG_gen = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    data = {'ErrMessage':ErrMessage, 'E_T':E_T, 'E_ST':E_ST, 'E_L':E_L, 'E_W':E_W, 'E_V':E_V, 'E_C':E_C, 'E_H':E_H, 'E_SL':E_SL, 'E_SW':E_SW, 'E_SV':E_SV, 'E_SC':E_SC, 'E_SH':E_SH, 'E_S':E_S, 'E_M':E_M, 'E_SM':E_SM, 'E_PV_sell':E_PV_sell, 'E_PV_gen':E_PV_gen, 'E_CG_gen':E_CG_gen, }
    return data

@login_required
def spec_calc_test(request, pk, house_pk):
    import sys
    from io import BytesIO
    import base64
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    builder = get_object_or_404(HouseBuilder, pk=pk)
    house = get_object_or_404(HouseBasic, builder__pk=pk, pk=house_pk)
    specs = HouseSpec.objects.filter(builder=builder).filter(house=house)
    calcs = HouseSpec.objects.filter(builder=builder).filter(house=house).filter(calc_done=False)

    data_list = []
    for spec in specs:
        xml, data = makeXMLtest(spec)
        data_list.append(data)
    
    context = {'builder': builder, 'house':house, 'specs':specs, 'calcs':calcs, 'data_list':data_list}
    return render(request, 'spec_calc_test.html', context)

def makeXMLtest(i):
    import urllib.request, urllib.error, urllib.parse
    import xml.etree.ElementTree as ET

    #HouseBasic
    model  = '<House FileVer="1" Name="' + i.house.name + '" Type="Standard,Independent" TotalArea="' + str(i.house.total_area) + '">'
    model += '<Environment Region="' + str(i.house.region) + '" AnnualSolarLevel="' + i.house.annual_solar_level + '" />'
    model += '<Zones>'
    model += '<Zone Type="LDK" Area="' + str(i.house.ldk_area) + '" NaturalWind="' + str(i.house.ldk_natural_wind) + '" />'
    model += '<Zone Type="Other" Area="' + str(i.house.ldk_area) + '" NaturalWind="' + str(i.house.oth_natural_wind) + '" />'
    model += '</Zones>'
    model += '<Envelope HeatStorage="' + i.house.heat_storage + '" EvaluationMethod="Real" TotalEnvelopeArea="' + str(i.house.total_envelope_area) + '" UAValue="' + str(i.house.ua_value) + '" SummerHAValue="' + str(i.house.summer_ha_value) + '" WinterHAValue="' + str(i.house.winter_ha_value) + '" />'
        
    #Heating
    if i.heating_system == 'RoomSpaceHeating':
        model += '<Heating Type="Individual">'
        if i.ldk_heating_type == 'RoomAirConditioningHeating':
            model += '<RoomAirConditioningHeating Zone="LDK" Efficiency="' + i.ldk_ac_heating_efficiency + '" Compressor="' + i.ldk_ac_heating_compressor + '" />'
        elif i.ldk_heating_type == 'FFHeating':
            if i.ldk_ff_saving_input:
                model += '<FFHeating Zone="LDK" Efficiency="' + str(i.ldk_ff_heating_efficiency) + '" />'
            else:
                model += '<FFHeating Zone="LDK" />'
        elif i.ldk_heating_type in ['PanelRadiator', 'HotWaterFloorHeatingRadiator', 'FanConvectorRadiator', ]:
            if i.ldk_heating_type == 'HotWaterFloorHeatingRadiator':
                model += '<HotWaterFloorHeatingRadiator Zone="LDK" AreaRate="' + str(i.ldk_hotwater_floorheating_area_rate) + '"  UpwardHeatFlowRate="' + str(i.ldk_hotwater_floorheating_upward_heatflow_rate) + '"/>'
            else:
                model += '<' + i.ldk_heating_type + ' Zone="LDK" />'

            if i.hotwater_heating_system == 'NonIntegrated':
                if i.hotwater_heating_source_type in ['OilClassic', 'GasClassic', 'GasLatentHeatRecovery', ]:
                    if i.hotwater_heating_source_saving_input:
                        if i.hotwater_heating_source_type == 'OilClassic':
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Efficiency="' + str(i.hotwater_heating_source_efficiency_OilClassic) + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                        elif i.hotwater_heating_source_type == 'GasClassic':
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Efficiency="' + str(i.hotwater_heating_source_efficiency_GasClassic) + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                        elif i.hotwater_heating_source_type == 'GasLatentHeatRecovery':
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Efficiency="' + str(i.hotwater_heating_source_efficiency_GasLatentHeatRecovery) + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                        else:
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                    else:
                        model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                elif i.hotwater_heating_source_type in ['OilLatentHeatRecovery', 'ElectricHeatPump', 'ElectricHeater', ]:
                    model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                else:
                    model += '<HotwaterHeatSource Type="NotUsed" Pipe="' + i.hotwater_heating_source_pipe + '" />'
            elif i.hotwater_heating_system in ['Integrated', 'Cogeneration', ]:
                model += '<HotwaterHeatSource Type="' + i.hotwater_heating_system + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
            elif i.hotwater_heating_system == 'Other':
                model += '<HotwaterHeatSource Name="' + i.hotwater_heating_source_name + '" Type="Other" Pipe="' + i.hotwater_heating_source_pipe + '" />'
            else:
                model += '<HotwaterHeatSource Type="NotUsed" Pipe="' + i.hotwater_heating_source_pipe + '" />'
        elif i.ldk_heating_type == 'ElecricFloorHeating':
            model += '<ElecricFloorHeating Zone="LDK" AreaRate="' + str(i.ldk_elecric_floorheating_area_rate) + '"  UpwardHeatFlowRate="' + str(i.ldk_elecric_floorheating_upward_heatflow_rate) + '"/>'
        elif i.ldk_heating_type == 'ElectricRoomHeaterWithThermalStorage':
            model += '<ElectricRoomHeaterWithThermalStorage Zone="LDK" />'
        elif i.ldk_heating_type == 'FloorHeatingWithRAC':
            model += '<FloorHeatingWithRAC Zone="LDK" AreaRate="' + str(i.ldk_ac_floorheating_area_rate) + '"  UpwardHeatFlowRate="' + str(i.ldk_ac_floorheating_upward_heatflow_rate) + '" Pipe="' + i.ldk_ac_floorheating_pipe + '" />'
        elif i.ldk_heating_type == 'OtherHeatingDevice':
            model += '<OtherHeatingDevice Zone="LDK" Name="' + i.ldk_other_heating_device_name + '" />'
        else:
            model += '<NotInstalled Zone="LDK" />'

        if i.oth_heating_type == 'RoomAirConditioningHeating':
            model += '<RoomAirConditioningHeating Zone="Other" Efficiency="' + i.oth_ac_heating_efficiency + '" Compressor="' + i.oth_ac_heating_compressor + '" />'
        elif i.oth_heating_type == 'FFHeating':
            if i.oth_ff_saving_input:
                model += '<FFHeating Zone="Other" Efficiency="' + str(i.oth_ff_heating_efficiency) + '" />'
            else:
                model += '<FFHeating Zone="Other" />'
        elif i.oth_heating_type in ['PanelRadiator', 'HotWaterFloorHeatingRadiator', 'FanConvectorRadiator', ]:
            if i.oth_heating_type == 'HotWaterFloorHeatingRadiator':
                model += '<HotWaterFloorHeatingRadiator Zone="Other" AreaRate="' + str(i.oth_hotwater_floorheating_area_rate) + '"  UpwardHeatFlowRate="' + str(i.oth_hotwater_floorheating_upward_heatflow_rate) + '"/>'
            else:
                model += '<' + i.oth_heating_type + ' Zone="Other" />'

            if i.hotwater_heating_system == 'NonIntegrated':
                if i.hotwater_heating_source_type in ['OilClassic', 'GasClassic', 'GasLatentHeatRecovery', ]:
                    if i.hotwater_heating_source_saving_input:
                        if i.hotwater_heating_source_type == 'OilClassic':
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Efficiency="' + str(i.hotwater_heating_source_efficiency_OilClassic) + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                        elif i.hotwater_heating_source_type == 'GasClassic':
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Efficiency="' + str(i.hotwater_heating_source_efficiency_GasClassic) + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                        elif i.hotwater_heating_source_type == 'GasLatentHeatRecovery':
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Efficiency="' + str(i.hotwater_heating_source_efficiency_GasLatentHeatRecovery) + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                        else:
                            model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                    else:
                        model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                elif i.hotwater_heating_source_type in ['OilLatentHeatRecovery', 'ElectricHeatPump', 'ElectricHeater', ]:
                    model += '<HotwaterHeatSource Type="' + i.hotwater_heating_source_type + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
                else:
                    model += '<HotwaterHeatSource Type="NotUsed" Pipe="' + i.hotwater_heating_source_pipe + '" />'
            elif i.hotwater_heating_system in ['Integrated', 'Cogeneration', ]:
                model += '<HotwaterHeatSource Type="' + i.hotwater_heating_system + '" Pipe="' + i.hotwater_heating_source_pipe + '" />'
            elif i.hotwater_heating_system == 'Other':
                model += '<HotwaterHeatSource Name="' + i.hotwater_heating_source_name + '" Type="Other" Pipe="' + i.hotwater_heating_source_pipe + '" />'
            else:
                model += '<HotwaterHeatSource Type="NotUsed" Pipe="' + i.hotwater_heating_source_pipe + '" />'
        elif i.oth_heating_type == 'ElecricFloorHeating':
            model += '<ElecricFloorHeating Zone="Other" AreaRate="' + str(i.oth_elecric_floorheating_area_rate) + '"  UpwardHeatFlowRate="' + str(i.oth_elecric_floorheating_upward_heatflow_rate) + '"/>'
        elif i.oth_heating_type == 'ElectricRoomHeaterWithThermalStorage':
            model += '<ElectricRoomHeaterWithThermalStorage Zone="Other" />'
        elif i.oth_heating_type == 'FloorHeatingWithRAC':
            model += '<FloorHeatingWithRAC Zone="Other" AreaRate="' + str(i.oth_ac_floorheating_area_rate) + '"  UpwardHeatFlowRate="' + str(i.oth_ac_floorheating_upward_heatflow_rate) + '" Pipe="' + i.oth_ac_floorheating_pipe + '" />'
        elif i.oth_heating_type == 'OtherHeatingDevice':
            model += '<OtherHeatingDevice Zone="Other" Name="' + i.oth_other_heating_device_name + '" />'
        else:
            model += '<NotInstalled Zone="Other" />'
    elif i.heating_system == 'AllSpaceHeating':
        model += '<Heating Type="Central">'
        if i.heating_rated_input:
            model += '<ElectricHeatPumpCentralHeating RatedPower="' + str(i.heating_rated_power) + '" RatedCapacity="' + str(i.heating_rated_capacity) + '" PowerCorrection="' + i.heating_power_correction + '" Coefficient="' + str(i.heating_coefficient) + '" />'
        else:
            model += '<ElectricHeatPumpCentralHeating PowerCorrection="' + i.heating_power_correction + '" Coefficient="' + str(i.heating_coefficient) + '" />'
    else:
        model += '<Heating Type="NotInstalled">'
    model += '</Heating>'

    #Cooling
    if i.cooling_system == 'RoomSpaceCooling':
        model += '<Cooling Type="Individual">'
        if i.ldk_cooling_type == 'RoomAirConditioningCooling':
            model += '<RoomAirConditioningCooling Zone="LDK" Efficiency="' + i.ldk_ac_cooling_efficiency + '" Compressor="' + i.ldk_ac_cooling_compressor + '" />'
        elif i.ldk_cooling_type == 'OtherCoolingDevice':
            model += '<OtherCoolingDevice Zone="LDK" Name="' + i.ldk_other_cooling_device_name + '" />'
        else:
            model += '<NotInstalled Zone="LDK" />'

        if i.oth_cooling_type == 'RoomAirConditioningCooling':
            model += '<RoomAirConditioningCooling Zone="Other" Efficiency="' + i.oth_ac_cooling_efficiency + '" Compressor="' + i.oth_ac_cooling_compressor + '" />'
        elif i.oth_cooling_type == 'OtherCoolingDevice':
            model += '<OtherCoolingDevice Zone="Other" Name="' + i.oth_other_cooling_device_name + '" />'
        else:
            model += '<NotInstalled Zone="Other" />'
    elif i.cooling_system == 'AllSpaceCooling':
        model += '<Cooling Type="Central">'
        if i.cooling_rated_input:
            model += '<ElectricHeatPumpCentralCooling RatedPower="' + str(i.cooling_rated_power) + '" RatedCapacity="' + str(i.cooling_rated_capacity) + '" PowerCorrection="' + i.cooling_power_correction + '" Coefficient="' + str(i.cooling_coefficient) + '" />'
        else:
            model += '<ElectricHeatPumpCentralCooling PowerCorrection="' + i.cooling_power_correction + '" Coefficient="' + str(i.cooling_coefficient) + '" />'
    else:
        model += '<Cooling Type="NotInstalled">'
    model += '</Cooling>'
    
    #Ventilation
    #model += '<Ventilation Type="DuctVentilation1" Saving="ThickDuctAndDCMotor" HeatExchanger="HeatExchanger" Frequency="HalfPerHour" Efficiency="0.95" HeatExchangerEfficiency="80" HeatExchangerLeak="1.00" HeatExchangerBal="0.90" />'
    #model += '''<Ventilation Type="DuctVentilation1" Saving="''' + i.ventilation_saving +'''" HeatExchanger="HeatExchanger" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" HeatExchangerEfficiency="'''+ str(i.ventilation_heatexchanger_efficiency) +'''" HeatExchangerLeak="'''+ str(i.ventilation_heatexchanger_leak) +'''" HeatExchangerBal="'''+ str(i.ventilation_heatexchanger_bal) +'''" />'''

    if i.ventilation_type == 'DuctVenitlation1':
        if i.ventilation_heatexchanger == 'HeatExchanger':
            if i.ventilation_saving in ['ThickDuctOnly', 'ThickDuctAndDCMotor', ]:
                model += '''<Ventilation Type="DuctVentilation1" Saving="''' + i.ventilation_saving +'''" HeatExchanger="HeatExchanger" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" HeatExchangerEfficiency="'''+ str(i.ventilation_heatexchanger_efficiency) +'''" HeatExchangerLeak="'''+ str(i.ventilation_heatexchanger_leak) +'''" HeatExchangerBal="'''+ str(i.ventilation_heatexchanger_bal) +'''" />'''
            elif i.ventilation_saving == 'SFP':
                model += '''<Ventilation Type="DuctVentilation1" SFP="''' + str(i.ventilation_sfp) + '''" HeatExchanger="HeatExchanger" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" HeatExchangerEfficiency="'''+ str(i.ventilation_heatexchanger_efficiency) +'''" HeatExchangerLeak="'''+ str(i.ventilation_heatexchanger_leak) +'''" HeatExchangerBal="'''+ str(i.ventilation_heatexchanger_bal) +'''" />'''
            else:
                model += '''<Ventilation Type="DuctVentilation1" HeatExchanger="HeatExchanger" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" HeatExchangerEfficiency="'''+ str(i.ventilation_heatexchanger_efficiency) +'''" HeatExchangerLeak="'''+ str(i.ventilation_heatexchanger_leak) +'''" HeatExchangerBal="'''+ str(i.ventilation_heatexchanger_bal) +'''" />'''
        else:
            if i.ventilation_saving in ['ThickDuctOnly', 'ThickDuctAndDCMotor', ]:
                model += '''<Ventilation Type="DuctVentilation1" Saving="''' + i.ventilation_saving +'''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" />'''
            elif i.ventilation_saving == 'SFP':
                model += '''<Ventilation Type="DuctVentilation1" SFP="''' + str(i.ventilation_sfp) + '''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" />'''
            else:
                model += '''<Ventilation Type="DuctVentilation1" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" />'''
    elif i.ventilation_type == 'DuctVentilation2or3':
        if i.ventilation_saving in ['ThickDuctOnly', 'ThickDuctAndDCMotor', ]:
            model += '''<Ventilation Type="''' + i.ventilation_type + '''" Saving="''' + i.ventilation_saving + '''" HeatExchanger="None" Frequency="''' + i.ventilation_frequency + '''" Efficiency="1" />'''
        elif i.ventilation_saving == 'SFP':
            model += '''<Ventilation Type="'''+ i.ventilation_type + '''" SFP="'''+ str(i.ventilation_sfp) + '''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency + '''" Efficiency="1" />'''
        else:
            model += '''<Ventilation Type="'''+ i.ventilation_type + '''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency + '''" Efficiency="1" />'''
    elif i.ventilation_type == 'WallMount1':
        if i.ventilation_heatexchanger == 'HeatExchanger':
            if i.ventilation_saving == 'SFP':
                model += '''<Ventilation Type="'''+ i.ventilation_type + '''" SFP="'''+ str(i.ventilation_sfp) + '''" HeatExchanger="HeatExchanger" Frequency="'''+ i.ventilation_frequency + '''" Efficiency="'''+ str(i.ventilation_efficiency) + '''" HeatExchangerEfficiency="'''+ str(i.ventilation_heatexchanger_efficiency) + '''" HeatExchangerLeak="'''+ str(i.ventilation_heatexchanger_leak) + '''" HeatExchangerBal="'''+ str(i.ventilation_heatexchanger_bal) +'''" />'''
            else:
                model += '''<Ventilation Type="'''+ i.ventilation_type + '''" HeatExchanger="HeatExchanger" Frequency="'''+ i.ventilation_frequency + '''" Efficiency="'''+ str(i.ventilation_efficiency) + '''" HeatExchangerEfficiency="'''+ str(i.ventilation_heatexchanger_efficiency) + '''" HeatExchangerLeak="'''+ str(i.ventilation_heatexchanger_leak) +'''" HeatExchangerBal="'''+ str(i.ventilation_heatexchanger_bal) + '''" />'''
        else:
            if i.ventilation_saving == 'SFP':
                model += '''<Ventilation Type="'''+ i.ventilation_type +'''" SFP="'''+ str(i.ventilation_sfp) +'''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" />'''
            else:
                model += '''<Ventilation Type="'''+ i.ventilation_type +'''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="'''+ str(i.ventilation_efficiency) +'''" />'''
    elif i.ventilation_type == 'WallMount2or3':
        if i.ventilation_saving == 'SFP':
            model += '''<Ventilation Type="'''+ i.ventilation_type +'''" SFP="'''+ str(i.ventilation_sfp) +'''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="1" />'''
        else:
            model += '''<Ventilation Type="'''+ i.ventilation_type +'''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="1" />'''
    else:
        if i.ventilation_saving in ['ThickDuctOnly', 'ThickDuctAndDCMotor', ]:
            model += '''<Ventilation Type="'''+ i.ventilation_type +'''" Saving="'''+ i.ventilation_saving +'''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency +'''" Efficiency="1" />'''
        elif i.ventilation_saving == 'SFP':
            model += '''<Ventilation Type="'''+ i.ventilation_type +'''" SFP="'''+ str(i.ventilation_sfp) +'''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency + '''" Efficiency="1" />'''
        else:
            model += '''<Ventilation Type="'''+ i.ventilation_type + '''" HeatExchanger="None" Frequency="'''+ i.ventilation_frequency + '''" Efficiency="1" />'''
    
    #Hotwater
    if i.bathroom in ['TapAndBath', 'TapOnly']:
        model += '<Hotwater>'
        if i.hotwater_heating_system == 'NonIntegrated':
            if i.water_heater_type == 'GasClassic':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="GasClassic" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasClassic_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="GasClassic" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasClassic_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="GasClassic" EfficiencyType="None" />'
            elif i.water_heater_type == 'GasLatentHeatRecovery':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="GasLatentHeatRecovery" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="GasLatentHeatRecovery" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="GasLatentHeatRecovery" EfficiencyType="None" />'
            elif i.water_heater_type == 'OilClassic':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="OilClassic" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilClassic_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="OilClassic" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilClassic_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="OilClassic" EfficiencyType="None" />'
            elif i.water_heater_type == 'OilLatentHeatRecovery':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="OilLatentHeatRecovery" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="OilLatentHeatRecovery" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="OilLatentHeatRecovery" EfficiencyType="None" />'
            elif i.water_heater_type == 'ElectricHeatPump':
                if i.heatpump_water_heater_efficiency_type == 'M1SEJISEfficiency':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="ElectricHeatPump" Name="'+ i.water_heater_name +'" EfficiencyType="M1SEJISEfficiency" JISEfficiency="'+ str(i.heatpump_water_heater_jis_efficiency_M1SEJISEfficiency) +'" />'
                elif i.heatpump_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="ElectricHeatPump" EfficiencyType="Other" JISEfficiency="'+ str(i.heatpump_water_heater_jis_efficiency_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="ElectricHeatPump" EfficiencyType="None" />'
            elif i.water_heater_type == 'Hybrid':
                if i.water_heater_heatpump_unit_input:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="Hybrid" HeatPumpUnit="RHP-R222(E)" TankUnit="RTU-R505(E)-U" BackupBoiler="RHBF-RK205SAT" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="Hybrid" HeatPumpUnit="'+ i.water_heater_heatpump_unit_coolant +'" TankCapacity="'+ i.water_heater_tank_capacity +'" />'
            elif i.water_heater_type == 'ElectricHeater':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="ElectricHeater" />'
            elif i.water_heater_type == 'Cogeneration':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="Cogeneration" />'
            elif i.water_heater_type == 'Other':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="Other" />'
            else:
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="NotUsed" />'
        elif i.hotwater_heating_system == 'Integrated':
            if i.integrated_water_heater_type == 'IntegratedGasClassic':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedGasClassic" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasClassic_Mode) +'" HeatingJISEfficiency="'+ str(i.gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedGasClassic" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasClassic_Other) +'" HeatingJISEfficiency="'+ str(i.gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedGasClassic" EfficiencyType="None" />'
            elif i.integrated_water_heater_type == 'IntegratedGasLatentHeatRecovery':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedGasLatentHeatRecovery" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Mode) +'" HeatingJISEfficiency="'+ str(i.gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedGasLatentHeatRecovery" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Other) +'" HeatingJISEfficiency="'+ str(i.gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedGasLatentHeatRecovery" EfficiencyType="None" />'
            elif i.integrated_water_heater_type == 'IntegratedOil':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedOil" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilClassic_Mode) +'" HeatingJISEfficiency="'+ str(i.gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedOil" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilClassic_Other) +'" HeatingJISEfficiency="'+ str(i.gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedOil" EfficiencyType="None" />'
            elif i.integrated_water_heater_type == 'IntegratedOilLatentHeatRecovery':
                if i.gasoil_water_heater_efficiency_type == 'Mode':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedOilLatentHeatRecovery" EfficiencyType="Mode" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Mode) +'" />'
                elif i.gasoil_water_heater_efficiency_type == 'Other':
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedOilLatentHeatRecovery" EfficiencyType="Other" JISEfficiency="'+ str(i.gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other) +'" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedOilLatentHeatRecovery" EfficiencyType="None" />'
            elif i.integrated_water_heater_type == 'Hybrid_Gas':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="Hybrid_Gas" TankPlace="'+ i.water_heater_tank_place +'" />'
            elif i.integrated_water_heater_type == 'Hybrid_Hybrid':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="Hybrid_Hybrid" />'
            elif i.integrated_water_heater_type == 'Gas_Hybrid':
                if i.water_heater_heatpump_unit_input:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="Gas_Hybrid" HeatPumpUnit="RHP-R222(E)" TankUnit="RTU-R505(E)-U" BackupBoiler="RHBF-RK205SAT" />'
                else:
                    model += '<WaterHeater Install="'+ i.bathroom +'" Type="Gas_Hybrid" HeatPumpUnit="'+ i.water_heater_heatpump_unit_coolant +'" TankCapacity="'+ i.water_heater_tank_capacity +'" />'
            elif i.integrated_water_heater_type == 'IntegratedElectricHeater':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="IntegratedElectricHeater" />'
            elif i.integrated_water_heater_type == 'Cogeneration':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="Cogeneration" />'
            elif i.integrated_water_heater_type == 'Other':
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="Other" />'
            else:
                model += '<WaterHeater Install="'+ i.bathroom +'" Type="NotUsed" />'
        elif i.hotwater_heating_system == 'Cogeneration':
            model += '<WaterHeater Install="'+ i.bathroom +'" Type="Cogeneration" />'
        elif i.hotwater_heating_system == 'Other':
            model += '<WaterHeater Install="'+ i.bathroom +'" Type="Other" Name="'+ i.water_heater_name +'" />'
        else:
            model += '<WaterHeater Install="'+ i.bathroom +'" Type="NotUsed" />'

        #model += '<WaterHeater Install="TapAndBath" Type="IntegratedOilLatentHeatRecovery" EfficiencyType="Other" JISEfficiency="95" />'
        model += '<Bath Function="'+ i.bath_function +'" Insulation="'+ i.bath_insulation +'" />'
        model += '<Pipe Type="'+ i.pipe_type +'" Saving="'+ i.pipe_saving +'" />'

        if i.bathroom == 'TapAndBath':
            model += '<Tap Type="BathShower" Saving="'+ i.bath_shower_tap_saving +'" />'
            model += '<Tap Type="Kitchen" Saving="'+ i.kitchen_tap_saving +'" />'
            model += '<Tap Type="WashBowl" Saving="'+ i.wash_bowl_tap_saving +'" />'
        elif i.bathroom == 'TapOnly':
            model += '<Tap Type="Kitchen" Saving="'+ i.kitchen_tap_saving +'" />'
            model += '<Tap Type="WashBowl" Saving="'+ i.wash_bowl_tap_saving +'" />'
        else:
            pass

        model += '</Hotwater>'
    else:
        pass


    #Lighting
    model += '<Lighting>'
    model += '<LightingZone Zone="MainZone" Efficiency="LED" Multi="Single" Dimming="Dimming" />'
    model += '<LightingZone Zone="OtherZone" Efficiency="LED" Dimming="Dimming" />'
    model += '<LightingZone Zone="NonLivingZone" Efficiency="LED" Sensor="Sensor" />'
    model += '</Lighting>'

    #Photovoltaic
    model += '<Photovoltaic PowerConditionerEfficiency="95">'
    model += '<PhotovoltaicPanel Capacity="5.88" Cell="Silicon" Setup="RoofMount" Direction="EastWest15" Angle="20" />'
    model += '</Photovoltaic>'
    model += '</House>'

    ################################################################
    data = "<request><model>{}</model></request>".format(model)
    data = data.encode('utf-8')

    req = urllib.request.Request('http://house.app.lowenergy.jp/api/v1/eval', data=data)
    req.add_header('Content-type', 'application/xml; charset=utf-8')
    req.add_header('Accept', 'application/xml')
    res = urllib.request.urlopen(req)
    xml = res.read()

    if format(ET.fromstring(xml).findtext('error')) == 'None':
        ErrMessage = None
        E_T = float(format(ET.fromstring(xml).findtext('E_T')))
        E_ST = float(format(ET.fromstring(xml).findtext('E_ST')))
        E_L = float(format(ET.fromstring(xml).findtext('E_L')))
        E_W = float(format(ET.fromstring(xml).findtext('E_W')))
        E_V = float(format(ET.fromstring(xml).findtext('E_V')))
        E_C = float(format(ET.fromstring(xml).findtext('E_C')))
        E_H = float(format(ET.fromstring(xml).findtext('E_H')))
        E_SL = float(format(ET.fromstring(xml).findtext('E_SL')))
        E_SW = float(format(ET.fromstring(xml).findtext('E_SW')))
        E_SV = float(format(ET.fromstring(xml).findtext('E_SV')))
        E_SC = float(format(ET.fromstring(xml).findtext('E_SC')))
        E_SH = float(format(ET.fromstring(xml).findtext('E_SH')))
        E_S = float(format(ET.fromstring(xml).findtext('E_S')))
        E_M = float(format(ET.fromstring(xml).findtext('E_M')))
        E_SM = float(format(ET.fromstring(xml).findtext('E_SM')))
        E_PV_sell = float(format(ET.fromstring(xml).findtext('E_PV_sell')))
        E_PV_gen = float(format(ET.fromstring(xml).findtext('E_PV_gen')))
        if format(ET.fromstring(xml).findtext('E_CG_gen')) == 'None':
            E_CG_gen = 0
        else:
            E_CG_gen = float(format(ET.fromstring(xml).findtext('E_CG_gen')))
    else:
        ErrMessage = format(ET.fromstring(xml).findtext('error'))
        E_T, E_ST, E_L, E_W, E_V, E_C, E_H, E_SL, E_SW, E_SV, E_SC, E_SH, E_S, E_M, E_SM, E_PV_sell, E_PV_gen, E_CG_gen = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    vals = {'ErrMessage':ErrMessage, 'E_T':E_T, 'E_ST':E_ST, 'E_L':E_L, 'E_W':E_W, 'E_V':E_V, 'E_C':E_C, 'E_H':E_H, 'E_SL':E_SL, 'E_SW':E_SW, 'E_SV':E_SV, 'E_SC':E_SC, 'E_SH':E_SH, 'E_S':E_S, 'E_M':E_M, 'E_SM':E_SM, 'E_PV_sell':E_PV_sell, 'E_PV_gen':E_PV_gen, 'E_CG_gen':E_CG_gen, }
    return xml, vals


