import React from 'react';
import {
  ResponsiveContainer,
  AreaChart,
  Area,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Legend
} from 'recharts';
import { LineChart, Sparkles } from 'lucide-react';

export function GrowthForecastChart({ forecast }) {
  if (!forecast || !forecast.daily_points) return null;

  // Filter every 4th day for a clean X-axis on smaller screens
  const chartData = forecast.daily_points.map((p) => ({
    date: p.date.slice(5), // 'MM-DD'
    predicted: p.predicted_subs,
    lower: p.lower_bound,
    upper: p.upper_bound,
  }));

  return (
    <div className="bg-[#141d2f]/90 border border-slate-800 rounded-2xl p-6 mb-8">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6">
        <div>
          <div className="flex items-center gap-2">
            <LineChart className="w-5 h-5 text-indigo-400" />
            <h3 className="text-lg font-bold text-white">30-Day Predictive Growth Forecast</h3>
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Modeled using Time-Series Regression with confidence interval bounds
          </p>
        </div>

        {/* Quick summary stats */}
        <div className="flex items-center gap-4 bg-slate-800/60 border border-slate-700/50 rounded-xl px-4 py-2">
          <div>
            <span className="text-[10px] text-slate-400 uppercase tracking-wider block">Projected 30d Subs</span>
            <span className="text-base font-extrabold text-white">
              {forecast.forecast_30d_subs.toLocaleString()}
            </span>
          </div>
          <div className="border-l border-slate-700 pl-4">
            <span className="text-[10px] text-slate-400 uppercase tracking-wider block">Net Gain</span>
            <span className="text-base font-extrabold text-emerald-400 flex items-center gap-1">
              +{forecast.predicted_sub_gain.toLocaleString()} ({forecast.growth_rate_pct}%)
            </span>
          </div>
        </div>
      </div>

      <div className="w-full h-72">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={chartData} margin={{ top: 10, right: 10, left: -10, bottom: 0 }}>
            <defs>
              <linearGradient id="predictedGrad" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#6366f1" stopOpacity={0.4} />
                <stop offset="95%" stopColor="#6366f1" stopOpacity={0.0} />
              </linearGradient>
              <linearGradient id="boundGrad" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#10b981" stopOpacity={0.15} />
                <stop offset="95%" stopColor="#10b981" stopOpacity={0.0} />
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
            <XAxis dataKey="date" stroke="#64748b" fontSize={12} tickLine={false} />
            <YAxis
              stroke="#64748b"
              fontSize={12}
              tickLine={false}
              domain={['dataMin - 200', 'dataMax + 200']}
              tickFormatter={(val) => `${(val / 1000).toFixed(1)}k`}
            />
            <Tooltip
              contentStyle={{
                backgroundColor: '#0f172a',
                borderColor: '#334155',
                borderRadius: '0.75rem',
                color: '#f8fafc',
                fontSize: '12px'
              }}
              formatter={(value, name) => [
                Number(value).toLocaleString(),
                name === 'predicted' ? 'Projected' : name === 'upper' ? 'Upper Bound' : 'Lower Bound'
              ]}
            />
            <Legend
              wrapperStyle={{ fontSize: '12px', paddingTop: '10px' }}
              formatter={(value) => (value === 'predicted' ? 'Projected Trajectory' : value === 'upper' ? 'Upper Confidence (95%)' : 'Lower Confidence (95%)')}
            />
            <Area
              type="monotone"
              dataKey="upper"
              stroke="#10b981"
              strokeDasharray="4 4"
              fillOpacity={1}
              fill="url(#boundGrad)"
            />
            <Area
              type="monotone"
              dataKey="lower"
              stroke="#64748b"
              strokeDasharray="4 4"
              fillOpacity={0}
            />
            <Area
              type="monotone"
              dataKey="predicted"
              stroke="#6366f1"
              strokeWidth={3}
              fillOpacity={1}
              fill="url(#predictedGrad)"
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
